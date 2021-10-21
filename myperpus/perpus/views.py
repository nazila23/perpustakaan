from django.shortcuts import redirect, render
from . import models

def form_pinjam(request):
    if request.POST:
        models.pinjam.objects.create(
            nmr_anggota = request.POST ['na'],
            nama = request.POST ['np'],
            buku = request.POST ['nb'],
            jml_buku = request.POST ['jb'],
            tgl_pinjam = request.POST ['tp'],
            tgl_kembali = request.POST ['tk'], 
            )
        return redirect(request, '/form_pinjam')
    data2 = models.pinjam.objects.all()
    return render(request, 'form_pinjam.html', {
            'isi':data2
            })
# def deleteindex(request,id):
#     models.makanan.objects.filter(pk=id).delete()
#     return redirect ('index')
    
# def detailindex(request,id):
#     detail = models.makanan.objects.filter(pk=id).first()
#     return render (request,'detail.html', {
#         'data': detail,
#     })
# def updateindex(request,id):
#     if request.POST:
#         models.makanan.objects.filter(id=id).update(
#             nama= request.POST ['nama'],
#             jenis= request.POST ['jenis'],
#             harga= request.POST ['harga'],
#             )
#     data = models.makanan.objects.filter(pk=id).first()
#     print(data)
#     return render (request,'edit.html',{
#         "data": data,
#     })