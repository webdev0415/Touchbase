import graphene
import requests
import base64
import environ
from django.conf import settings
from apps.payments.models import Transaction
from apps.payments.obj_types import TransactionType

p = settings.PAYPAL

# ptc = paypal-transaction-complete, just making it more vague
class PTC(graphene.Mutation):
    """ Mutation for processing a payment """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        order_id = graphene.String(required=True)
        phone = graphene.String(required=True)

    # 1. Get order_id, setup basic_auth variable
    def mutate(self, info, order_id, phone):
        erl = []
        if info.context.user.is_authenticated:
            user = info.context.user
            t = Transaction()
            t.user = user
            t.payment_id = order_id
            t.payer_ipv4 = info.context.META['REMOTE_ADDR']
            
            #string to go into basic auth
                # bas_c = f'{ PAYPAL_CLIENT }'
                # bas_s = f'{ PAYPAL_SECRET }'
                # b_c_basic_auth = base64.b64encode(bas_c.encode('utf-8'))
                # b_s_basic_auth = base64.b64encode(bas_s.encode('utf-8'))

                # ba_user = b_c_basic_auth.decode("utf-8").replace('=', '')
                # ba_pass = b_s_basic_auth.decode("utf-8").replace('=', '')
                # print(ba_user, '~~~~', ba_pass)
            
            # 2. Get an access token from the PayPal API
            # Import access token var from settings
            # If None, get an access token. If expired, get new
            # Upon getting new, save that back to the var
            # Above is setup, then use the var in any subsequent requests

            if not p['ACCESS_TOKEN']:
                auth = requests.post(
                    p['OAUTH_API'],
                    headers=p['AT_HEADERS'],
                    auth=p['AT_AUTH'],
                    data=p['AT_DATA']
                )
                # set p.ACCESS_TOKEN to returned access token
                p['ACCESS_TOKEN'] = auth.json()['access_token']
            
            # check expiration

            # print('memes3', p['ORDER_API'] + order_id)
            # 3. Call PayPal to get the transaction details
            details = requests.get(
                p['ORDER_API'] + order_id,
                headers={
                    'Accept': 'application/json',
                    'Authorization': f"Bearer { p['ACCESS_TOKEN'] }"
                }
            )

            details = details.json()

            # 4. Handle any errors from the call
            if 'error' in details:
                # return paypal's error message too
                erl.append('PaypalError')

            ## put these in try catch, if fails, append the same err
            # 5. Validate the transaction details are as expected
            if not details['purchase_units'][0]['amount']['value'] == '29.99' and details['purchase_units'][0]['amount']['currency_code'] == 'USD':
                erl.append('PriceError')

            if not details['id'] == order_id and details['intent'] == 'CAPTURE' and details['purchase_units'][0]['payee']['merchant_id'] == p['MERCHANT_ID']:
                erl.append('IntegrityError')

            

            # 6. Save the transaction to DB
                # Enable bool for correct plan
            user.settings.haspSPF = True

            t.payer_id = details['payer']['payer_id']
            t.payment_status = details['status']
            t.price_total = details['purchase_units'][0]['amount']['value']
            t.billing_state = details['purchase_units'][0]['shipping']['address']['admin_area_1']
            t.billing_city = details['purchase_units'][0]['shipping']['address']['admin_area_2']
            t.billing_country = details['purchase_units'][0]['shipping']['address']['country_code']
            t.billing_first_name = details['payer']['name']['given_name']
            t.billing_last_name = details['payer']['name']['surname']
                # get billing phone from graphql mutation
            t.billing_phone = phone
            t.billing_email = details['payer']['email_address']
            
            # try catch
            # NOTE: use update_fields to minimize load!
            t.save()
            user.settings.save()

            # 7. Return success
            if len(erl) > 0:
                return PTC(success=False, errors=erl)
            return PTC(success=True)