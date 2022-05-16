from AmazonInteractions import AmazonTest


class TestPathToCartRegisteredUser:
    '''Test Scenario to simulate of a basic registered user behaviour:
    log in, search for a product, add from search to cart, proceed to cart,
    then delete product from a cart, and log out'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_signIn(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signIn()
        assert amazon_class_instance.Is_loggedin == True

    def test_search_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.search()
        assert amazon_class_instance.Is_search_result == True

    def test_open_product_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.open_from_search()
        assert amazon_class_instance.Is_page == True

    def test_add_to_cart_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.buy_from_pdp()
        assert amazon_class_instance.Cart_empty == False

    def test_open_cart_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.open_cart()
        assert amazon_class_instance.Is_page == True

    def test_delete_from_cart_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.delete_from_cart()
        assert amazon_class_instance.Cart_empty == True

    def test_sign_out(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signOut
        assert amazon_class_instance.Is_loggedin == False


class TestPathToCartNonRegisteredUser:
    '''Test Scenario to simulate of a non-registered user behaviour:
    search for a product, add to cart from search, proceed to cart,
    then clear cart - 6 tests total'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_search_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.search()
        assert amazon_class_instance.Is_search_result == True

    def test_open_product_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.open_from_search()
        assert amazon_class_instance.Is_page == True

    def test_add_to_cart_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.buy_from_pdp()
        assert amazon_class_instance.Cart_empty == False

    def test_open_cart_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.open_cart()
        assert amazon_class_instance.Is_page == True

    def test_delete_from_cart_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.delete_from_cart()
        assert amazon_class_instance.Cart_empty == True


class TestTopMenuRegisteredUsers:
    '''Set of tests to test that top menu links are working for signed in user
    There are between 10-12 top links (varies), so we test 12 (max) links'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_signIn(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signIn()
        assert amazon_class_instance.Is_loggedin == True

    def test_top_link_1_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(1)
        assert amazon_class_instance.Is_page == True

    def test_top_link_2_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(2)
        assert amazon_class_instance.Is_page == True

    def test_top_link_3_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(3)
        assert amazon_class_instance.Is_page == True

    def test_top_link_4_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(4)
        assert amazon_class_instance.Is_page == True

    def test_top_link_5_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(5)
        assert amazon_class_instance.Is_page == True

    def test_top_link_6_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(6)
        assert amazon_class_instance.Is_page == True

    def test_top_link_7_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(7)
        assert amazon_class_instance.Is_page == True

    def test_top_link_8_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(8)
        assert amazon_class_instance.Is_page == True

    def test_top_link_9_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(9)
        assert amazon_class_instance.Is_page == True

    def test_top_link_10_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(10)
        assert amazon_class_instance.Is_page == True

    def test_top_link_11_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(11)
        assert amazon_class_instance.Is_page == True

    def test_top_link_12_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(12)
        assert amazon_class_instance.Is_page == True

    def test_sign_out(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signOut
        assert amazon_class_instance.Is_loggedin == False


class TestTopMenuNonRegisteredUsers:
    '''Set of tests to test that top menu links are working for NOT signed in user
    There are between 10-12 top links (varies), so we test 12 (max) links'''
    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_top_link_1_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(1)
        assert amazon_class_instance.Is_page == True

    def test_top_link_2_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(2)
        assert amazon_class_instance.Is_page == True

    def test_top_link_3_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(3)
        assert amazon_class_instance.Is_page == True

    def test_top_link_4_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(4)
        assert amazon_class_instance.Is_page == True

    def test_top_link_5_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(5)
        assert amazon_class_instance.Is_page == True

    def test_top_link_6_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(6)
        assert amazon_class_instance.Is_page == True

    def test_top_link_7_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(7)
        assert amazon_class_instance.Is_page == True

    def test_top_link_8_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(8)
        assert amazon_class_instance.Is_page == True

    def test_top_link_9_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(9)
        assert amazon_class_instance.Is_page == True

    def test_top_link_10_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(10)
        assert amazon_class_instance.Is_page == True

    def test_top_link_11_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(11)
        assert amazon_class_instance.Is_page == True

    def test_top_link_12_not_signed_in(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.top_link(12)
        assert amazon_class_instance.Is_page == True

class TestPaginatorPage2SignedIn:
    '''Testing paginator transition to page 2 of search results -- signed in'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_signIn(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signIn()
        assert amazon_class_instance.Is_loggedin == True

    def test_search(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.search()
        assert amazon_class_instance.Is_search_result == True

    def test_goPage(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.goPage()
        assert amazon_class_instance.Is_page == True

    def test_sign_out(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signOut
        assert amazon_class_instance.Is_loggedin == False


class TestPaginatorPage2NotSignedIn:
    '''Testing paginator transition to page 2 of search results -- NOT signed in'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_search(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.search()
        assert amazon_class_instance.Is_search_result == True

    def test_goPage(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.goPage()
        assert amazon_class_instance.Is_page == True

class TestWishList:

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_signIn(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signIn()
        assert amazon_class_instance.Is_loggedin == True

    def test_search(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.search()
        assert amazon_class_instance.Is_search_result == True

    def test_open_product(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.open_from_search()
        assert amazon_class_instance.Is_page == True

    def test_addList(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.addList()
        assert amazon_class_instance.Is_page == True

    def test_sign_out(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.signOut
        assert amazon_class_instance.Is_loggedin == False


class TestPostalCodeEntry:
    '''Test entry fields for postal code for non registered users'''

    def test_getPage(self):
        amazon_class_instance = AmazonTest()
        assert amazon_class_instance.getPage() == "https://www.amazon.ca/"

    def test_enter_postal_code(self):
        amazon_class_instance = AmazonTest()
        amazon_class_instance.enter_address()
        assert amazon_class_instance.Is_page == True
        # we destroy driver here as this is the last test
        amazon_class_instance.destroyDriver()


