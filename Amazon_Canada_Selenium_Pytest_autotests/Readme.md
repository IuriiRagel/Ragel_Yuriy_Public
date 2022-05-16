<h1> Automated tests with Selenium and Pytest framework for Amazon Canada website </h1>

You will find 58 tests developed for Amazon Canada testing, which test basic functionality of Amazon website
b
<h2> Prerequisites </h2>
<ul> 
  <li> Python </li>
  <li> Pytest package installed </li>
  <li> Selenium package installed </li>
  <li> Google Chrome Webdriver should be launched and active (you can adjust the webdriver in configs file -- see below) </li>
 </ul>
 
 <h2> Files and descriptions (folder tests) </h2>
 <ul>
  <li> <i> configs.py </i> -- file contains configurations (email and password, search term, webdriver used for tests) </li>
  <li> <i> AmazonInteractions.py </i> -- this script contains class AmazonTest with methods for various interactions on Amazon website (sign in, sign out, product search, adding to cart, clear cart etc.). These methods are used to build particular tests </li>
  <li> <i> AmazonTestScenarios </i> -- each class inside this script represents a particular Test Scenario with detailed tests inside them. You can launch the full script or each scenario separately. See below for each Test Scenario description and tests implemented within each scenario </li>
 
  <h2> Test Scenarios and tests descriptions </h2>
  <ol type="1">
    <li> <b> TestPathToCartRegisteredUser = 8 tests </b> 
      <br> Test scenario for path to cart for a <u> signed in </u> user: open wesbite, log in, search for products, open product page, add to cart, open cart, delete from cart, sign out </li>
    <br>
    <li> <b> TestPathToCartNonRegisteredUser = 6 tests </b>
      <br> Test scenario for path to cart for a <u> non-registered </u> user (without a sign in): open wesbite, log in, search for products, open product page, add to cart, open cart, delete from cart, sign out </li>
    <br>
    <li> <b> TestTopMenuRegisteredUsers = 15 tests </b>
      <br> Test sccenario to test links from a top menu for a signed in user (max posssible links are 12. Failed tests signify that the links are missing): log in, click each link in the top menu, sign out </li>
    <br>
    <li> <b> TestTopMenuNonRegisteredUsers = 13 tests </b>
      <br> Test scenario to test links from a top menu for not signed in user (max posssible links are 12. Failed tests signify that the links are missing): click each link in the top menu </li>
    <br>
    <li> <b> TestPaginatorPage2SignedIn = 5 tests </b>
      <br> Test scenario to test paginator on search results page for a signed in user: sign in, search, click on page 2 in paginator, sign out </li>
    <br>
    <li> <b> TestPaginatorPage2NotSignedIn = 3 tests </b>
      <br> Test scenario to test paginator on search results page for not signed in user: sign in, search, click on page 2 in paginator, sign out </li>
    <br>
    <li> <b> TestWishList = 6 tests </b>
      <br> Test scenario to test item adding to wish list with new wish list creation. Screenshot is being saved in the tests folder of the new wishlist. Each wishlist is named in a convention: "Testing_shopping_list_dd/mm/YY HH:MM" to be able to track when the wish list has been created. Tests include WebDriver.Wait, to wait for items to be interactable </li>
    <br>
    <li> <b> TestPostalCodeEntry = 2 tests </b>
      <br> Test scenario on adding postal code into the pop up field on main page. We are using WebDriver.Wait to wait for fields to be clickable to be able to enter a sample postal code </li>
    
    <h2> Important Notes </h2>
    Please note, that in order to avoid CAPTCHA during Sign In, we have implemented time.sleep() periods to simulate slow entry of username and password. This helped to avoid the CAPTCHA. When launching script from different regions, Amazon might trigger security warning for Amazon. In that case you may use any other valid Amazon accounr credentials (just update them in configs.py file)
