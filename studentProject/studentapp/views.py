from django.shortcuts import render,redirect
from studentapp import forms
import json
from csv import reader
import pandas as pd
import os
from csv import DictReader
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your views here.


def check_RollNo(form):
		df = pd.read_csv("student.csv")
		found=False
		if df.empty:
			print("empty data")
		else:
			for ind in df.index:
				if str(df['RollNumber'][ind]) ==form.cleaned_data['RollNumber']:
					found=True
					break;
		return found;

def StudentView(request):
	form = forms.StudentForm()
	if request.method == 'POST':
		form = forms.StudentForm(request.POST)
		if form.is_valid():
			data = {}
			import csv
			from csv import DictWriter
			import csv 
			field_names = ['Name','RollNumber','Age',
						   'Gender']
			# data rows of csv file
			dict = form.cleaned_data
			# name of csv file
			filename = "student.csv"
			if not (os.path.isfile(filename)):
			# writing to csv file
				with open(filename, 'w') as csvfile: 
					# creating a csv writer object
					csvwriter = csv.writer(csvfile) 
					# writing the fields
					csvwriter.writerow(field_names)
					csvfile.close()
			found=check_RollNo(form)
			if found:
				error='please check Roll Number, A student is registed with the following Roll Number'
				#raise ValidationError('please check Roll Number, A student is registed with the following Roll Number')
				return render(request,'studentapp/register.html',{'error':error,'form':form})
			# list of column names
			from csv import DictReader
			# open file in read mode
			with open('student.csv', 'a') as f_object:
				dictwriter_object = DictWriter(f_object, fieldnames=field_names)
				#Pass the dictionary as an argument to the Writerow()
				dictwriter_object.writerow(dict)
				#Close the file object
				f_object.close()
			return redirect('/')
	return render(request,'studentapp/register.html',{'form':form})

def studentHomeview(request):
	filename = 'student.csv'
	list_students = []
	if  os.path.isfile(filename):
		# open file in read mode
		with open('student.csv', 'r') as read_obj:
			# pass the file object to DictReader() to get the DictReader object
			csv_dict_reader = DictReader(read_obj)
			
			# iterate over each line as a ordered dictionary
			for row in csv_dict_reader:
				# row variable is a dictionary that represents a row in csv
				list_students.append(row)
	return render(request,'studentapp/home.html',{'details':list_students})

def updatehomeview(request,id):
	with open('student.csv', 'r') as read_obj:
		# pass the file object to DictReader() to get the DictReader object
		csv_dict_reader = DictReader(read_obj)
		list_students = []
		found = False
		index = -1
		# iterate over each line as a ordered dictionary
		for row in csv_dict_reader:
			index+=1
			# row variable is a dictionary that represents a row in csv
			print(row['RollNumber'])
			if row['RollNumber'] == str(id):
				found = True
				student = row
				break
			list_students.append(row)
		if found:
			print(student)
		if request.method == 'POST':
			form = forms.StudentForm(request.POST)
			if form.is_valid():
				df = pd.read_csv("student.csv")
				# updating the column value/data
				df.loc[index, 'Name'] = form.cleaned_data['Name']
				df.loc[index, 'RollNumber'] = form.cleaned_data['RollNumber']
				df.loc[index, 'Age'] = form.cleaned_data['Age']
				df.loc[index, 'Gender'] = form.cleaned_data['Gender']
				# writing into the file
				df.to_csv("student.csv", index=False)
  
				print(df)
				return redirect('/')
	return render(request,'studentapp/update.html',{'student':student})

def searchView(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		with open('student.csv', 'r') as read_obj:
			csv_dict_reader = DictReader(read_obj)
			list_students = []
			for row in csv_dict_reader:
				if row['Name'].lower().find(searched.lower()) != -1:
					list_students.append(row)
	return render(request,'studentapp/search.html',{'searched':searched,'list_students':list_students})


			




