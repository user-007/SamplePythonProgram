class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us", self.contactWebsite)
class MacBook(Apple):
    def __init__(self):
        self.yearOfManifacture = 2017
    def manufactureDetails(self):
        print("This MacBook was manifactured in the year {} by {}".format(self.yearOfManifacture, self.manufacturer))

macbook = MacBook()
macbook.manufactureDetails()
macbook.contactDetails()

