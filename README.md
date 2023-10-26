# DashAppCourse
Repository for Plotly-Dash course exercises.

## Week 1:
### Resources - Dash Fundamentals 

WasmDash for building Dash apps on the browser: https://wasmdash.vercel.app/ 

Installation guide for local Dash app development: [Tech stack](https://open-resources.github.io/dash_curriculum/part1/chapter0.html)

Datasets to be used throughout the course: [agriculture](https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv), [makeup](https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/shades.csv)

[Dash in 20 tutorial](https://dash.plotly.com/tutorial#connect-to-data:-code-breakdown)

Dash Core Components: https://dash.plotly.com/dash-core-components

Dash html Button component: https://dash.plotly.com/dash-html-components/button

Tables with Dash Ag Grid
[Getting Started](https://dash.plotly.com/dash-ag-grid/getting-started)
Recommended chapters for more advanced learning: [Pagination](https://dash.plotly.com/dash-ag-grid/pagination), [Column filters](https://dash.plotly.com/dash-ag-grid/column-filters), [Cell editing](https://dash.plotly.com/dash-ag-grid/cell-editing)

[Graphing Library](https://plotly.com/python/)

Plotly Express Graphs:<br>
[Graph attributes](https://plotly.com/python-api-reference/plotly.express.html)


### Resources - Dash Interactivity 

WasmDash for building Dash apps on the browser: https://wasmdash.vercel.app/ 

Installation guide for local Dash app development: [Tech stack](https://open-resources.github.io/dash_curriculum/part1/chapter0.html)

Datasets to be used throughout the course: [agriculture](https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv), [makeup](https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/shades.csv)

[The Callback](https://open-resources.github.io/dash_curriculum/part1/chapter4.html)

[Supplement video tutorial on the callback](https://youtu.be/pNMWbY0AUJ0)

[Plotly Histogram](https://plotly.com/python/histograms/)

[Dash Input Component](https://dash.plotly.com/dash-core-components/input)

[Plotly Dash Forum](https://community.plotly.com/)



## Week2:
### Resources - Building Graphs

WasmDash for building Dash apps on the browser: https://wasmdash.vercel.app/

Datasets to be used throughout the course: [agriculture](https://github.com/plotly/datasets/blob/master/Dash-Course/US-Exports/2011_us_ag_exports.csv), [makeup](https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/shades.csv)

Plotly Python [graphing docs](https://plotly.com/python/)

Plotly Express: intro to the [high-level interface](https://plotly.com/python-api-reference/plotly.express.html)

[Plotly Figure Reference](https://plotly.com/python/reference/index/)

The Dash Core [Graph Component](https://dash.plotly.com/dash-core-components/graph)


### Resources - Advanced Applications

Dash Bootstrap: [choosing and declaring the stylesheet/theme](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)

List of [all available themes](https://bootswatch.com/default/)

[Rows and Columns](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) to position your app components neatly on the page

[dbc.Button()](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/)

[Dash Bootstrap styling cheat sheet](https://dashcheatsheet.pythonanywhere.com/)

Advanced Callbacks:
- [State argument:](https://dash.plotly.com/basic-callbacks#dash-app-with-state)<br>
   commonly used when there are certain components in the callback Input that should not trigger the callback. For example,     a dropdown combined with a button; the dropdown would be assigned to the State and the button to the Input.
- [no_update:](https://dash.plotly.com/advanced-callbacks#displaying-errors-with-dash.no_update)<br>
   used at the end of the function when you don’t want certain Output components to update.
- [duplicate_outputs: ](https://dash.plotly.com/duplicate-callback-outputs)<br>
   needs to be added when you use the same component ID AND Property in the Output within two different callbacks.
- [prevent_initial_call](https://dash.plotly.com/advanced-callbacks#prevent-callback-execution-upon-initial-component-render)<br>
  used if you don’t want the callback to trigger when the app first loads or anytime the app (browser) is refreshed. 

Expanding your component collection:
- [Upload for csv](https://dash.plotly.com/dash-core-components/upload); Upload for [images](https://dash.plotly.com/dash-core-components/upload#displaying-uploaded-images). (not on WasmDash)
- [Interval](https://dash.plotly.com/dash-core-components/interval) component
- [Modal](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/): first example with this [WasmDash modal code](https://github.com/plotly/tutorial-code/blob/main/session4/modal_example.py).



## Week3:
### Resources - App Deployment and Resources

[Render.com](https://dashboard.render.com/)

#### Deployed example on Render with data coming in through http link:
[deploy-app-example-repo](https://github.com/Coding-with-Adam/deploy-app-example/tree/main)
 
##### Prepare your App on Pycharm: 
1. Open Pycharm and activate venv:<br>
   ```.\venv\Scripts\activate```
2. Install all libraries and gunicorn in your virtual environment
3. Create requirements file:<br>
   ```pip freeze > requirements.txt```
4. Make sure your app code has<br>
   ```server = app.server```
5. Run app to make sure it works:<br>
   python app.py
6. Push code to your github account; how-to see: https://youtu.be/vpRkAoCqX3o 

##### Deploy App to the Web with Render
how-to see: https://youtu.be/H16dZMYmvqo?feature=shared 

7. Open your Render account
8. Create new Web Service and choose: “Build and deploy from a Git repository”
9. Add the url of your public git repository
10. Give the app a unique name
11. Update the gunicorn command to:<br>
    ```gunicorn app_name:server```<br>
    (Note: uvicorn can be used as well, see app conditions you have implemented)

Note: Possible error:<br>
Render won’t work with the latest version of certain python libraries. For example, you’ll get an error if your requirements.txt file has the most recent version of pandas. Render allows up to pandas==1.3.5

#### Deployed example on Render with data in local csv sheet:
[deploy-app2-example-repo](https://github.com/Coding-with-Adam/deploy-app2-example)

- When your app has a local csv sheet you’re pulling data from, the file structure should look like this: [deploy-app2-example-repo](https://github.com/Coding-with-Adam/deploy-app2-example)
- Notice how you would [read the csv sheet into your app](https://github.com/Coding-with-Adam/deploy-app2-example/blob/main/src/app.py)
- Don’t forget to add to your app code:<br>
```server = app.server```
- And install _gunicorn_ or _uvicorn_ in your virtual environment
- When deploying the app on Render.com, ensure that the Root Directory is _src_

<br>

[Resources for future Dash learning](https://drive.google.com/file/d/16989ZAMGjVGnLYTzQshLQRGhVs8mZCFR/view?usp=sharing)

Make use of community Dash knowledge on the forum: https://community.plotly.com/ 

