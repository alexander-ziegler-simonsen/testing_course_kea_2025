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


### recording end-2-end testing

run this 
```bash
npx cypress open
```
(which opens a new window)

this record part, was not that easy to find, here is the list.
- click end-2-end
- - pick chrome and start tests (opens new window)
- - - click "new spec" -> create new -> give it a name -> run it
- - - - click "studio beta" in top right corner -> "ai text" click new test -> give it a name -> click
- - - - - now you record every step (if you are slow on the keyboard, it will be saved as wait time inbetween clicks)

 ## playwright

we start with this command:
```bash
npm init playwright@latest
```

other commands you will need
```bash
npx playwright test
npx playwright show-report
npx playwright test --ui

npx playwright --version

# how to update it 
npm install -D @playwright/test@latest
npx playwright install --with-deps

# for recording tests
npx playwright codegen
```
when you are using codegen, keep in mind, that you dont save a file, that is something you your self have to do after it is done.