def index(request):

    show = GaspricesShowprice.gastype
    search_list = GaspricesShowprice.objects.all()

    obj = get_object_or_404(findlocation, id = 1)
    
    form = EmailSignupForm()

    context1 = {
        'address1' : obj,
        'show' : show,
        'form': form,
        # 'map' : m
    }

    return render(request, 'pages/new_index.html', context1)
