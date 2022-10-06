from django.shortcuts import render, redirect
from . import models
from django.forms import inlineformset_factory

# Create your views here.

def dashboard(request):
    jumlahproduk = models.produk.objects.all().count()
    return render(request, 'dashboard.html',{ 
        "jumlahproduk" : jumlahproduk,
    })

#ENTITAS PRODUK
def dataproduk(request):
    allprodukobj = models.produk.objects.all()

    return render (request, 'dataproduk.html' ,{
        'allprodukobj' : allprodukobj,
    })

def createproduk(request):
    if request.method == "GET":
        return render(request, 'createproduk.html')
    else:
        nama = request.POST['nama']
        satuan = request.POST['satuan']
        harga = request.POST['harga']
        kategori = request.POST['kategori']

        newproduk = models.produk(
            namaproduk = nama,
            satuanproduk = satuan,
            hargaproduk = harga,
            kategoriproduk = kategori
        )
        newproduk.save()
        return redirect('dataproduk')

def updateproduk(request, id):
    produkobj = models.produk.objects.get(idproduk = id)
    if request.method == "GET":
        return render(request, 'updateproduk.html' ,{
            'allprodukobj' : produkobj
        })
    else:
        produkobj.namaproduk = request.POST['nama']
        produkobj.satuanproduk = request.POST['satuan']
        produkobj.hargaproduk = request.POST['harga']
        produkobj.kategoriproduk = request.POST['kategori']
        produkobj.save()
        return redirect('dataproduk')

def deleteproduk(request, id):
    produkobj = models.produk.objects.get(idproduk = id)
    produkobj.delete()
    return redirect('dataproduk')

#ENTITAS KARYAWAN
def datakaryawan(request):
    allkaryawanobj = models.karyawan.objects.all()

    return render (request, 'datakaryawan.html' ,{
        'allkaryawanobj' : allkaryawanobj,
    })

def createkaryawan(request):
    if request.method == "GET":
        return render(request, 'createkaryawan.html')
    else:
        karyawan = request.POST['karyawan']
        kontak = request.POST['kontak']
        jobdesc = request.POST['jobdesk']

        newkaryawan = models.karyawan(
            namakaryawan = karyawan,
            kontakkaryawan = kontak,
            jobdesk = jobdesc
        )
        newkaryawan.save()
        return redirect('datakaryawan')

def updatekaryawan(request, id):
    karyawanobj = models.karyawan.objects.get(idkaryawan = id)
    if request.method == "GET":
        return render(request, 'updatekaryawan.html' ,{
            'allkaryawanobj' : karyawanobj
        })
    else:
        karyawanobj.namakaryawan = request.POST['karyawan']
        karyawanobj.kontakkaryawan = request.POST['kontak']
        karyawanobj.jobdesk = request.POST['jobdesk']
        karyawanobj.save()
        return redirect('datakaryawan')

def deletekaryawan(request, id):
    karyawanobj = models.karyawan.objects.get(idkaryawan = id)
    karyawanobj.delete()
    return redirect('datakaryawan')

#ENTITAS PEMBELIAN
def datapembelian(request):
    allpembelianobj = models.pembelian.objects.all()
    allkaryawanobj = models.karyawan.objects.all()

    return render (request, 'datapembelian.html' ,{
        'allpembelianobj' : allpembelianobj,
        'allkaryawanobj' : allkaryawanobj
    })

def createpembelian(request):
    allkaryawanobj = models.karyawan.objects.all()
    if request.method == "GET":
        return render(request, 'createpembelian.html' ,{
        'allkaryawanobj' : allkaryawanobj
    })
    else:
        id_karyawan = request.POST['id_karyawan']
        getidkaryawan = models.karyawan.objects.get(idkaryawan=id_karyawan)
        tanggal = request.POST['tanggal']
        supplier = request.POST['supplier']

        newpembelian = models.pembelian(
            idkaryawan = getidkaryawan,
            tanggaltransaksi = tanggal,
            namasupplier = supplier
        )
        newpembelian.save()
        return redirect('datapembelian')

def updatepembelian(request, id):
    pembelianobj = models.pembelian.objects.get(idpembelian = id)
    if request.method == "GET":
        allkaryawanobj = models.karyawan.objects.all()
        return render(request, 'updatepembelian.html' ,{
            'allpembelianobj' : pembelianobj,
            'allkaryawanobj' :allkaryawanobj
            
        })
    else:
        idkaryawan = request.POST['id_karyawan']
        pembelianobj.tanggaltransaksi = request.POST['tanggal']
        pembelianobj.namasupplier = request.POST['supplier']
        getkaryawanobj = models.karyawan.objects.get(idkaryawan = idkaryawan)
        pembelianobj.idkaryawan = getkaryawanobj
        pembelianobj.save()
        return redirect('datapembelian')

def deletepembelian(request, id):
    pembelianobj = models.pembelian.objects.get(idpembelian = id)
    pembelianobj.delete()
    return redirect('datapembelian')

#PENJUALAN
def datapenjualan(request):
    allpenjualanobj = models.penjualan.objects.all()
    allkaryawanobj = models.karyawan.objects.all()

    return render (request, 'datapenjualan.html' ,{
        'allpenjualanobj' : allpenjualanobj,
        'allkaryawanobj' : allkaryawanobj
    })

def createpenjualan(request):
    allkaryawanobj = models.karyawan.objects.all()
    if request.method == "GET":
        return render(request, 'createpenjualan.html' ,{
        'allkaryawanobj' : allkaryawanobj
    })
    else:
        id_karyawan = request.POST['id_karyawan']
        getidkaryawan = models.karyawan.objects.get(idkaryawan=id_karyawan)
        tanggaljual = request.POST['tanggaljual']
        pelanggan = request.POST['pelanggan']

        newpenjualan = models.penjualan(
            idkaryawan = getidkaryawan,
            tanggalpenjualan = tanggaljual,
            namapelanggan = pelanggan
        )
        newpenjualan.save()
        return redirect('datapenjualan')

def updatepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(idpenjualan = id)
    if request.method == "GET":
        allkaryawanobj = models.karyawan.objects.all()
        return render(request, 'updatepenjualan.html' ,{
            'allpenjualanobj' : penjualanobj,
            'allkaryawanobj' :allkaryawanobj
        })
    else:
        idkaryawan = request.POST['id_karyawan']
        penjualanobj.tanggalpenjualan = request.POST['tanggaljual']
        penjualanobj.namapelanggan = request.POST['pelanggan']
        getkaryawanobj = models.karyawan.objects.get(idkaryawan = idkaryawan)
        penjualanobj.idkaryawan = getkaryawanobj
        penjualanobj.save()
        return redirect('datapenjualan')

def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(idpenjualan = id)
    penjualanobj.delete()
    return redirect('datapenjualan')

#ENTITAS DETAIL PEMBELIAN
def createdetailpembelian(request, id):
    OrderFormSet = inlineformset_factory(models.pembelian, models.detailpembelian, fields = ('idproduk', 'kuantitasproduk'))
    pembelian = models.pembelian.objects.get(idpembelian = id)
    formset = OrderFormSet (instance = pembelian)
    if request.method == 'POST':
        formset = OrderFormSet (request.POST, instance = pembelian)
        if formset.is_valid():
            formset.save()
            return redirect('datapembelian')
    context = {'formset' : formset}
    return render (request, 'createdetailpembelian.html', context)

#ENTITAS DETAIL PENJUALAN
def createdetailpenjualan(request, id):
    OrderFormSet = inlineformset_factory(models.penjualan, models.detailpenjualan, fields = ('idproduk', 'kuantitasproduk'))
    penjualan = models.pembelian.objects.get(idpenjualan = id)
    formset = OrderFormSet (instance = penjualan)
    if request.method == 'POST':
        formset = OrderFormSet (request.POST, instance = penjualan)
        if formset.is_valid():
            formset.save()
            return redirect('datapenjualan')
    context = {'formset' : formset}
    return render (request, 'createdetailpenjualan.html', context)