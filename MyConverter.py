import streamlit as st
import pandas as pd
import requests
class Currency_convertor:
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()
		# Extracting only the rates from the json data
		self.rates = data["rates"]

	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency], 2)
		st.subheader('User Entered LENGTH OF PASSWORD ')
		st.write('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

YOUR_ACCESS_KEY='74d91ced9ab8bd40b34eb5ef4603a540'
# YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
c = Currency_convertor(url)


st.header("Online Currency Converter")
st.sidebar.header('Choose Currency')

From_Country = ['USD','INR','PKR','AUD','EUR','NGN','QAR']
from_country = st.sidebar.selectbox('Country From ', From_Country, 1)

To_Country = ['USD','INR','PKR','AUD','EUR','NGN','QAR']
to_country = st.sidebar.selectbox('To Country ', To_Country, 1)
amount=st.sidebar.number_input('Amount ')

st.sidebar.button('Calculate',c.convert(from_country, to_country, amount))
