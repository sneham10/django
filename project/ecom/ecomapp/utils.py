def upload_file(f):
    print(f)
    with open('ecomapp/uploads/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)