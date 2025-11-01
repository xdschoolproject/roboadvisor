from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home_page/home.html')


def stock_analysis(request):
    # Redirect to the Streamlit app URL (assuming it's running on localhost:8501)
    return redirect("http://localhost:8501")