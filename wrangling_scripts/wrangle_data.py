import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
	"""Creates four plotly visualizations

	Args:
		None

	Returns:
		list (dict): list containing the four plotly visualizations

	"""
	figures = []
	titles=[]
	
	# first chart plots arable land from 1990 to 2015 in top 10 economies 
	# as a line chart
	# Load the data
	df = pd.read_csv('wrangling_scripts/forest_cover.csv',skiprows=4)
	df_metadata = pd.read_csv('wrangling_scripts/country_metadata.csv')
	
	#Data cleaning
	df=df.drop([str(i) for i in range(1960,1990,1)]+['2022','2023','Unnamed: 68', 'Indicator Name','Indicator Code'],axis=1)
	df_metadata=df_metadata.drop('SpecialNotes',axis=1)
	
	df_metadata=pd.merge(df[['Country Name', 'Country Code']],df_metadata,on='Country Code')
	df=df.drop('Country Name',axis=1)
	
	df_m=df.melt(id_vars='Country Code',value_name='forested_area_perc',var_name='Year')
	df_m=df_m.rename(columns={'Country Code':'country_code'})
	df_m.Year=df_m.Year.astype(int)
	region_list = df_metadata.loc[df_metadata.Region.isna()]['Country Code'].tolist()
	
	for region in region_list:
		graph = []	  
		graph.append(
		  go.Scatter(
		  x = df_m.loc[df_m.country_code == region]['Year'].tolist(),
		  y = df_m.loc[df_m.country_code == region]['forested_area_perc'].tolist(),
		  mode = 'lines'
		  )
		)
		title_name=df_metadata[df_metadata['Country Code']==region].TableName.tolist()[0]
		layout = dict(title = title_name,
					xaxis = dict(title = 'Year'),
					yaxis = dict(title = 'Forested Area (%)'),
					)		
		figures.append(dict(data=graph, layout=layout))
		titles.append(title_name)
	
	# graph_one = []	  
	# graph_one.append(
	  # go.Scatter(
	  # x = [0, 1, 2, 3, 4, 5],
	  # y = [0, 2, 4, 6, 8, 10],
	  # mode = 'lines'
	  # )
	# )

	# layout_one = dict(title = 'Chart One',
				# xaxis = dict(title = 'x-axis label'),
				# yaxis = dict(title = 'y-axis label'),
				# )

# # second chart plots ararble land for 2015 as a bar chart	 
	# graph_two = []

	# graph_two.append(
	  # go.Bar(
	  # x = ['a', 'b', 'c', 'd', 'e'],
	  # y = [12, 9, 7, 5, 1],
	  # )
	# )

	# layout_two = dict(title = 'Chart Two',
				# xaxis = dict(title = 'x-axis label',),
				# yaxis = dict(title = 'y-axis label'),
				# )


# # third chart plots percent of population that is rural from 1990 to 2015
	# graph_three = []
	# graph_three.append(
	  # go.Scatter(
	  # x = [5, 4, 3, 2, 1, 0],
	  # y = [0, 2, 4, 6, 8, 10],
	  # mode = 'lines'
	  # )
	# )

	# layout_three = dict(title = 'Chart Three',
				# xaxis = dict(title = 'x-axis label'),
				# yaxis = dict(title = 'y-axis label')
					   # )
	
# # fourth chart shows rural population vs arable land
	# graph_four = []
	
	# graph_four.append(
	  # go.Scatter(
	  # x = [20, 40, 60, 80],
	  # y = [10, 20, 30, 40],
	  # mode = 'markers'
	  # )
	# )

	# layout_four = dict(title = 'Chart Four',
				# xaxis = dict(title = 'x-axis label'),
				# yaxis = dict(title = 'y-axis label'),
				# )
	
	# append all charts to the figures list
	# figures.append(dict(data=graph_one, layout=layout_one))
	# figures.append(dict(data=graph_two, layout=layout_two))
	# figures.append(dict(data=graph_three, layout=layout_three))
	# figures.append(dict(data=graph_four, layout=layout_four))
	l=len(titles)
	return figures,titles,l