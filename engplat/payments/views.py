from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.http import HttpResponse
from engplat import settings
from engplat.base.models import User
from engplat.payments.models import UserPayment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_TEST_API_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


@csrf_exempt
@login_required
def product_page(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                customer_email=request.user.email,
                ui_mode='embedded',
                line_items=[
                    {
                        'price': settings.PRICE_ID_30_DAYS,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                return_url=YOUR_DOMAIN + '/payments/return_page?session_id={CHECKOUT_SESSION_ID}',
            )
        except Exception as e:
            return str(e)
        return JsonResponse({'clientSecret': session.client_secret})
    return render(request, 'payments/product_page.html')


def return_page(request):
    return render(request, 'payments/return_page.html')


def session_status(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    return JsonResponse({'status': session.status, 'customer_email': session.customer_details.email})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    endpoint_secret = settings.WEBHOOK_SECRET_TEST
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        user_email = session.customer_email
        user = User.objects.get(email=user_email)
        user_payment = UserPayment(user=user, stripe_checkout_id=session_id)
        user_payment.save()

        if session.payment_status == 'paid':
            user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
            user_payment.payment_bool = True
            user_payment.save()

    elif event['type'] == 'checkout.session.async_payment_succeeded':
        session = event['data']['object']
        session_id = session.get('id', None)
        user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
        user_payment.payment_bool = True
        user_payment.save()

    elif event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']
        session_id = session.get('id', None)
        # user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
        # user_email = user_payment.user.email
        # send_mail(
        #     subject='Pagamento em English Learning Platform',
        #     message='Infelizmente seu pagamento não foi aprovado, por favor acesse a plataforma e tente novamente.',
        #     from_email='admin@admin.com',
        #     recipient_list=[f'{user_email}']
        # )

        # TODO: enviar e-mail ao cliente solicitando nova tentativa
    return HttpResponse(status=200)
