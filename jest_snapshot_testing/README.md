# Jest snapshot testing

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

This small project shows usage of [Jest](https://jestjs.io/docs) snapshot testing feature. It is a great way to test UI components and prevent form unexpected changes.
More about snapshot testing could be found [here](https://jestjs.io/docs/en/snapshot-testing)

##Starting 

After downloading this project follow those steps:
1. Install dependencies
```bash
npm install
```
2. Run script responsible for testing

```bash
npm run test
```

Testing process should finnish successfully, and it will be running in watch mode - it will rerun all test for each change. 
Like in the image below.

![](https://i.imgur.com/5nHger3.png)

Now lets change something

3. Go to `jest_snapshot_testing/src/components/Button.tsx` and change text within button

After saving a change testing script should react to it and rerun test again and as you can see test is failing.
This is due to the fact that saved snapshot of this component doesn't match to the active one.

![](https://i.imgur.com/jFd2FJj.png)

![](https://i.imgur.com/WLmRyXI.png)
Using available options from terminal window save a new snapshot. Now test is passing.

![](https://i.imgur.com/B75tbaT.png)

##How does it work
To fully understand how this feature works lets discuss code below
![](https://i.imgur.com/gwyo325.png)

So, function renderer generate DOM tree for tested components and transform it to JSON format. Then this tree is compared with tree structure saved in `jest_snapshot_testing/src/test/__snapshots__` directory.
When our snapshot test is failing we can simply replace a stored snapshot to the new one.
As previously said this feature might prevent unexpected changes in UI code.
