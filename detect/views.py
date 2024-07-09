from django.shortcuts import render
from joblib import load
# Create your views here.
model=load('churn_model.pkl')
def detection (request):
    if request.method=='POST':
        gender=request.POST['gender']
        SeniorCitizen=request.POST['seniorCitizen']
        Partner=request.POST['partner']
        Dependents=request.POST['dependents']
        tenure=request.POST['tenure']
        PhoneService=request.POST['phoneService']
        MultipleLines=request.POST['multipleLines']
        InternetService=request.POST['internetService']
        OnlineSecurity=request.POST['onlineSecurity']
        OnlineBackup=request.POST['onlineBackup']
        DeviceProtection=request.POST['deviceProtection']
        TechSupport=request.POST['techSupport']
        StreamingTV=request.POST['streamingTV']
        StreamingMovies=request.POST['streamingMovies']
        Contract=request.POST['contract']
        PaperlessBilling=request.POST['paperlessBilling']
        PaymentMethod=request.POST['paymentMethod']
        MonthlyCharges=request.POST['monthlyCharges']
        TotalCharges=request.POST['totalCharges']
        y_pred=model.predict([[gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]])
        if y_pred[0]==0:
            y_pred='Not Churn'
        else:
            y_pred='Churn'
        return render(request,'dash/detection.html',{'result':y_pred})
    return render(request,'dash/detection.html')

