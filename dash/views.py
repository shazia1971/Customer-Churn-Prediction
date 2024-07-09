import pandas as pd
from django.shortcuts import render
import os

""" def dashboard(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'Telco-Customer-Churn.csv')
    df = pd.read_csv(file_path)

    # Aggregations
    churn_count = df['Churn'].value_counts().to_dict()
    contract_counts = df['Contract'].value_counts().to_dict()
    monthly_charges = df.groupby('Churn')['MonthlyCharges'].mean().to_dict()
    churn_by_contract = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack().fillna(0).to_dict()
    tenure_by_churn = df.groupby('Churn')['tenure'].mean().to_dict()

    context = {
        'churn_count': churn_count,
        'contract_counts': contract_counts,
        'monthly_charges': monthly_charges,
        'churn_by_contract': churn_by_contract,
        'tenure_by_churn': tenure_by_churn,
    }
    return render(request, 'dash/dashboard.html', context)"""

import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def dashboard(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'Telco-Customer-Churn.csv')
    df = pd.read_csv(file_path)

    # Churn Count Pie Chart
    churn_count = df['Churn'].value_counts().reset_index()
    churn_count.columns = ['Churn', 'Count']
    fig_churn = px.pie(churn_count, values='Count', names='Churn')

    # Contract Types Bar Chart
    contract_counts = df['Contract'].value_counts().reset_index()
    contract_counts.columns = ['Contract', 'Count']
    fig_contract = px.bar(contract_counts, x='Contract', y='Count')

    # Average Monthly Charges Bar Chart
    monthly_charges = df.groupby('Churn')['MonthlyCharges'].mean().reset_index()
    fig_monthly_charges = px.bar(monthly_charges, x='Churn', y='MonthlyCharges')

    # Churn by Contract Type Bar Chart
    churn_by_contract = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack().fillna(0).reset_index()
    fig_churn_by_contract = go.Figure()
    for churn in ['Yes', 'No']:
        fig_churn_by_contract.add_trace(go.Bar(x=churn_by_contract['Contract'], y=churn_by_contract[churn]*100, name=churn))
    fig_churn_by_contract.update_layout(barmode='group')

    # Average Tenure by Churn Status Bar Chart
    tenure_by_churn = df.groupby('Churn')['tenure'].mean().reset_index()
    fig_tenure_by_churn = px.bar(tenure_by_churn, x='Churn', y='tenure')

    # Churn by Gender Bar Chart
    churn_by_gender = df.groupby('gender')['Churn'].value_counts(normalize=True).unstack().fillna(0).reset_index()
    fig_churn_by_gender = go.Figure()
    for churn in ['Yes', 'No']:
        fig_churn_by_gender.add_trace(go.Bar(x=churn_by_gender['gender'], y=churn_by_gender[churn]*100, name=churn))
    fig_churn_by_gender.update_layout(barmode='group')

    # Senior Citizen Distribution Pie Chart
    senior_citizen_count = df['SeniorCitizen'].value_counts().reset_index()
    senior_citizen_count.columns = ['SeniorCitizen', 'Count']
    fig_senior_citizen = px.pie(senior_citizen_count, values='Count', names='SeniorCitizen')

    # Dependents Distribution Pie Chart
    dependents_count = df['Dependents'].value_counts().reset_index()
    dependents_count.columns = ['Dependents', 'Count']
    fig_dependents = px.pie(dependents_count, values='Count', names='Dependents')

    # Paperless Billing Distribution Pie Chart
    paperless_billing_count = df['PaperlessBilling'].value_counts().reset_index()
    paperless_billing_count.columns = ['PaperlessBilling', 'Count']
    fig_paperless_billing = px.pie(paperless_billing_count, values='Count', names='PaperlessBilling')
    # Convert plots to HTML
    plots = {
        'churn': fig_churn.to_html(full_html=False),
        'contract': fig_contract.to_html(full_html=False),
        'monthly_charges': fig_monthly_charges.to_html(full_html=False),
        'churn_by_contract': fig_churn_by_contract.to_html(full_html=False),
        'tenure_by_churn': fig_tenure_by_churn.to_html(full_html=False),
        'churn_by_gender': fig_churn_by_gender.to_html(full_html=False),
        'senior_citizen': fig_senior_citizen.to_html(full_html=False),
        'dependents': fig_dependents.to_html(full_html=False),
        'paperless_billing': fig_paperless_billing.to_html(full_html=False),
    }

    return render(request, 'dash/dashboard.html', {'plots': plots})
