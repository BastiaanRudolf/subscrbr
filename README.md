# Subscrbr - Vue Static Web App Boilerplate

Hi! 👋 This repository contains the boilerplate code to create a simple static web app (SWA) called Subscrbr. This app lets users send their email for us to store in an Azure Storage Account table. The boilerplate is part of this blog, but you should also be able to do without it. Let me know if you have any questions!

## Requirements
* An Azure account with a subscription, create one for free [here](https://azure.microsoft.com/en-us/free/).
* [Python 3.9.9](https://www.python.org/downloads/release/python-399/) (Azure Functions unfortunately does not yet support 3.10 as of 2021-12-22)
* Install Azure Functions Core Tools v3.x by running `npm i -g azure-functions-core-tools@3 --unsafe-perm true` (for more info check [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local), if you don't have npm installed already, check [this](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) article)
* After cloning, `cd` into the project folder and run `npm i` to install required dependencies.
* Create a file called `local.settings.json` in the `api/` folder, with the following content (no worries, we're replacing the dummy value later):
```json
{
    "Host": {
      "CORS": "http://localhost:8080"
    },
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "example_STORAGE": "<Your-Access-Key>"
    }
}
```
* Create a `.env` file in your project root directory, with the following content:
```
VUE_APP_API="http://localhost:7071/api"
```
* (OPTIONAL) It's highly recommended to use VSCode with this repository, since it has some useful extensions, see `.vscode/extensions.json`.

## Setting up
* Complete steps in requirements first
* Push this code to your own GitHub repository.
* Create a static web app from that GitHub repository in the Azure Portal > Static Web Apps, see [here](https://docs.microsoft.com/en-us/azure/static-web-apps/get-started-portal?tabs=vanilla-javascript) for a quickstart. **IMPORTANT**: This step will generate your CI/CD, so once finished, `git pull` changes locally.
* Since an API endpoint is already configured, you need to create a Storage Account yourself, easiest is using the Azure Portal > Storage Accounts > Create, see [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal) for help.
* Copy your Storage Account Access key (navigate to your Storage Account > Access keys > Show Keys > Copy connection string of key1)
* Go to `local.settings.json` and paste this connection string as value for `example_STORAGE`.
* Navigate to your SWA in the Azure Portal, and go to Configuration, click Add for Application settings & add `example_STORAGE` as name, and your just copied connection string as value.
* You're all set! 🎉

## Starting up
* Run `npm run serve` in your product root folder to start the development server, and visit `http://localhost:8080/` to check if it works.
* In another terminal session, run `cd api/ && funct start` to start your API on `http://localhost:7071/` and check if it works.

## Pushing changes
One of the beautiful things of Azure SWA with GitHub, is that it uses GitHub actions for CI/CD. This means that whenever a change is made to your main branch, it will automatically be pushed to your web app!

## Resources
* A blog with more details about this setup
* More on Azure Static Web Apps
* More on Function Apps


If you like this boilerplate, and want to be notified when I create more of these, follow me on Twitter! 
[@bignonotation](https://twitter.com/bignonotation)

If you loved it, and want to buy me a coffee:<br>
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/bignonotation)