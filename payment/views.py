from django.shortcuts import render, HttpResponse
from django.views.generic import View
from payment.forms import CheckoutForm


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        template_name = 'shop/checkout.html'
        return render(self.request, template_name, {'form': form})
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse("<h1>Successfull your paymanent</h1><br><a href='/'>Back Home</a>")
