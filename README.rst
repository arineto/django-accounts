Django accounts
===============

This is a Django app that implements the auth functionalities

Install instructions
--------------------

.. code-block:: python

  pip install git+https://github.com/arineto/django-accounts.git


Use instructions
----------------

In your project settings add the following:

.. code-block:: python

  INSTALLED_APPS = [
      ...
      'accounts',
  ]

  LOGIN_URL = 'accounts:login'
  LOGOUT_URL = 'accounts:logout'
  LOGIN_REDIRECT_URL = 'Some URL from your project'

  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_USE_TLS = True
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'example@email.com'
  EMAIL_HOST_PASSWORD = 'email.password'

And you also need to add the app URLs:

.. code-block: python

  urlpatterns = [
    ...
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
  ]
