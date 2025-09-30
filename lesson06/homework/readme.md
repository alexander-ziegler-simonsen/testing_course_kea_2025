# the website that will be tested

Our goal is to learn how to write e2e tests.

The website will be testing have been given by our teacher.

## setup of the website locally

This is the link for the repo, which will be running locallly (it will not be copied into this folder):


https://github.com/arturomorarioja/js_webshop

it's easy, just use this command in our terminal: 
```bash
git clone https://github.com/arturomorarioja/js_webshop


cd js_webshop

code .
```

this will open the project inside vs code, then open the index file and click down in the right corner "go live" (which need the extension "Live Server" by Ritwick Dey)

# e2e testing

we have learned today about the 3 main e2e system used in tech companies.
- cypress
- playwright
- selenium

therefor it is really importent to learn how to use all 3 of them.

## cypress

first of all you need to make a folder, use the command 'npm init' and fill out what it asks.

then:

```bash
# npm install cypress --save-dev # old version

npm install -D cypress@15.3.0 --save-dev

# also add this plugin

npm i --save-dev cypress-codegen

# and add these
npm install –g eslint-plugin-cypress –save-devInstallation and Configuration


```
then we can start up the cypress control panel wtih this command:
```bash
npx cypress open

# later try this 
# npx cypress codegen # could not get it to work
```

cypress have a recording feature, so it will be faster to write your tests.
you need to open your cypress.config.js file and add this to it:

```javascript
module.exports = defineConfig({
  e2e: {
    experimentalStudio: true
  },
});
```
this will add it to the setup, so you can use it.


pick end-2-end testing


 