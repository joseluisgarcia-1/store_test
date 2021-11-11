from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from catalogo.apps.home.forms import ContactForm
# Create your views here.
def about_index(request):
    return HttpResponse("Index about")
#return render(request, 'about.html', {})

def contacto_view(request):
    info_enviado = ""
    email = ""
    title = ""
    text = ""
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
            """bloque información envio por email """
            to_admin = 'mailpruebapython@gmail.com'
            html_content = "Información recibidad de %s <br> -----Mensaje-----<br> %s" %(email,text)
            msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
            """fin del bloque"""
    else:
        formulario = ContactForm()
    ctx = {'form': formulario, 'email': email, 'title': title, 'text':text, 'info_enviado': info_enviado}
    return render(request, 'contacto.html', {'ctx': ctx})