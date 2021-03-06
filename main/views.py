# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render

from .forms import MerchantForm, InquiryForm
from .models import Merchant, Inquiry

from app.settings import CELERY_ACTIVE

if CELERY_ACTIVE:
    from .tasks import (
        task_new_merchant_sms_notification,
        task_email_notification,
    )
else:
    from .utils import send_sms_notification, send_email_notification


def home(request):
    template = 'main/home.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    context = {}
    return render(request, template, context)


def services(request):
    template = 'main/services.html'
    context = {}
    return render(request, template, context)


def contact(request):
    template = 'main/contact.html'
    form = InquiryForm
    context = {'form': form}
    return render(request, template, context)


def signup(request):
    template = 'main/signup.html'
    form = MerchantForm
    context = {'form': form}
    return render(request, template, context)


def m_signup(request):
    """
    process the Ajax form,
    js_file_ref: Merchant Signup form request
    - Adds a merchant to the database
    - Sends email to sales@themerchantaffiliate.com notifiying of new signup
    - sends an email to the user to confirm data submit (User email is from the form)
    """
    # check if the request is POST
    if request.method == 'POST':

        # Assign form fields to variables
        company = request.POST.get('company')
        salutation = request.POST.get('salutation')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        website = request.POST.get('website')
        street = request.POST.get('street')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        industry = request.POST.get('industry')
        salay = request.POST.get('salay')
        description = request.POST.get('description')
        bank = request.POST.get('bank')
        lead_source = request.POST.get('lead_source')
        contact_method = request.POST.get('contact_method')

        # Create an object
        merchant = Merchant()

        # Assign the form fields to the object
        merchant.company = company
        merchant.salutation = salutation
        merchant.f_name = f_name
        merchant.l_name = l_name
        merchant.email = email
        merchant.mobile = mobile
        merchant.website = website
        merchant.street = street
        merchant.state = state
        merchant.zip_code = zip_code
        merchant.city = city
        merchant.industry = industry
        merchant.salay = salay
        merchant.description = description
        merchant.bank = bank
        merchant.lead_source = lead_source
        merchant.contact_method = contact_method

        # Save the Object
        merchant.save()

        merchant_msg_text = "Your email has been submitted, Thank you! - TMA"
        #task_email_notification.delay(email, merchant_msg_text)  # with Celery

        send_email_notification(email, merchant_msg_text)  # without Celery

        # add task send email to us
        us = "sales@themerchantaffiliate.com"
        us_msg_text = "New Merchant registered \n Company: {0}".format(company)

        #task_email_notification.delay(us, us_msg_text)  # with Celery

        send_email_notification(us, us_msg_text) # without Celery

        # create reponse object
        success_response_text = {}
        error_response_text = {}

        # Successful Respnse text
        success_response_text['type'] = "S01"
        success_response_text['msg'] = "Your application has been submitted successfully!"

        # failed response text
        error_response_text['type'] = "E01"
        error_response_text['msg'] = "Something went wrong!"

        return HttpResponse(
            json.dumps(success_response_text),
            content_type = "application/json"
        )

    else:
        return HttpResponse(
            json.dumps(error_response_text),
            content_type = "application/json"
        )



def inquiry(request):
    """
    Process POST Ajax Form,
    js_file_ref: Inquiry form POST
    - Adds an inquiry to database
    - sends an email with the inquiry message and details to sales@themerchantaffiliate.com
    """
    # If request is POST
    if request.method == 'POST':

        # Assign the recieved form field to variables
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Assign the email address for email to be sent to
        us = "sales@themerchantaffiliate.com"
        # Assign the body text of the email
        msg_text = "Sender: {0} \n Phone: {1} \n Email: {2} \n Message: {3}".format(name, phone, email, message)

        # create a model Object to save to database
        inquiry = Inquiry()
        # Assign the form fields to the database model
        inquiry.name = name
        inquiry.phone = phone
        inquiry.email = email
        inquiry.message = message

        # save the model to the database
        inquiry.save()

        # add task send inquiery information
        #task_email_notification.delay(us, msg_text)  # with Celery
        send_email_notification(us, msg_text)  # without Celery

        # create response object
        success_response_text = {}
        error_response_text = {}
        # assign successful response object
        success_response_text['type'] = 'S01'
        success_response_text['msg'] = 'Message has been sent successfuly!'

        # assign failed response object
        error_response_text['type'] = 'E01'
        error_response_text['msg'] = 'Something went wrong!'

        # sends the response back to the browser
        return HttpResponse(
            json.dumps(success_response_text),
            content_type = "application/json"
        )

    else:
        # sends the response back too the browser
        HttpResponse(
            json.dumps(error_response_text),
            content_type = "application/json"
        )
