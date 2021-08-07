# Meow Sweden
### Handmade accessories and jewelry with cattitude =^.^=


![Responsive Image](assets/images/responsive-image.png)


## Project Goals
**What is it?** 
Meow Sweden is a webshop that provides handmade fancy and luxurious cat ears for all crazy catladies with a sence of fashion. Here can the cat fashionista be sure to find sparkely cat ears in different colors and styles. There is also a jewelry section with necklaces made with ancient Quipu code.

**Who is it for?**
For any catlover, male or female (yes, men can be catladies too), that like to level up their outfit.

**Why am I building it?**
This project is actually why I got into coding. I started up Meow Sweden in spring 2019 and started selling my cat ears and necklaces on **[Etsy](https://www.etsy.com/se-en/shop/MeowSweden?ref=seller-platform-mcnav)**. But I always felt like Meow Sweden should have its own homepage with it own webshop. And with this project I can finaly dive into how I would like it to be! And I can get full controll over all the design and all the functionallity.


## Table of Content

* [**UX**](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owner Goals](#site-owner-goals)
    * [Design](#design) 
* [**Wireframes and Flowcharts**](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
* [**Database Structrue**](#database-structure)
* [**Features**](#features)
* [**Technologies Used**](#technologies-used)
    * [Languages](#languages)
    * [Frameworks Libraries Programs](#frameworks-libraries-programs)
* [**Testing**](#testing)
    * [Bugs](#bugs)
    * [To Do](#to-do)
* [**Deployment**](#deployment)
    * [GitHub Pages](#gitHub-pages)
* [**Credits**](#credits)


## UX

### User Goals
* The website should be visually appeling 
* The website should work well on all devices
* The ladingpage should display some products making user motivated to continue browsing
* The users should be able to make a purchase
* The website should have some background informaion about the company

### User Stories

* As a user I want to be able to browse through the products by category
* As a user I want to be able to easily navigate the website
* As a user I want to be able to search for products
* As a user I want to see images and information of the product
* As a user I want to able to choose from a selection of colors when I buy some products 
* As a user I want to create a customer profile 
* As a user I want to be able to log in to that profile, and log out
* As a user I want to be able to view my shopping bag with added products and/or edit/delete it
* As a user I want to be able to pay for my order with a credit card
* As a user I want to recive a confirmation email when I make an order

### Site Owner Goals
* As a site owner I want to promomte my products to my users
* As a site owner I want to be able to see all the orders
* As a site owner I want to be able to see all registered users
* As a site owner I be able to log in and out of the admin profile
* As a site owner I want o be able to edit and delete products
* As a site owner I want o be able to add new products to the webshop


### Design

#### Fonts:

I used fonts from [Google Fonts](https://fonts.google.com/)
* [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond?query=cor) on h1
* [Raleway](https://fonts.google.com/specimen/Raleway?query=rale) on h2/h3
* [Roboto](https://fonts.google.com/specimen/Roboto) on paragraphs

#### Images:

All product images are me own and was photographed my me. Background images are from [Adobe](www.stock.adobe.com)

#### Color: 

I wanted to use colors that match background images and giving the website a luxurious feeling with some gold.

![Color palette](readme-images/meow-sweden-palette.png)

[Back to top](#table-of-content)


## Wireframes and Flowcharts
### Wireframes
[Balsamic](https://balsamiq.com) was used to create the wireframes for this project

* Desktop Wireframes
    * [HOME](wireframes/HOME-DeskTop.png)
    * [Products](wireframes/Products-DT.png)
    * [Product Detail](wireframes/ProdDetail-DT.png)
    * [About](wireframes/About-DT.png)
    * [Contact](wireframes/Contact-DT.png)
    * [Profile](wireframes/Profile-DT.png)
    * [Shopping Bag](wireframes/View-Shopping-Bag-DT.png)
    * [Checkout](wireframes/Checkout-DT.png)

    
* Tablet Wireframes
    * [HOME](wireframes/HOME-Tablet.png)
    * [Products](wireframes/Products-T.png)
    * [Product Detail](wireframes/ProdDetail-T.png)
    * [About](wireframes/About-T.png)
    * [Contact](wireframes/Contact-T.png)
    * [Profile](wireframes/Profile-T.png)
    * [Shopping Bag](wireframes/View-Shopping-Bag-T.png)
    * [Checkout](wireframes/Checkout-T.png)

* Smartphone Wireframes 
    * [HOME](wireframes/HOME-SmartPhone.png)
    * [Products](wireframes/Products-SP.png)
    * [Product Detail](wireframes/ProdDetails-SP.png)
    * [About](wireframes/About-SP.png)
    * [Contact](wireframes/Contact-SP.png)
    * [Profile](wireframes/Profile-SP.png)
    * [Shopping Bag](wireframes/View-Shopping-Bag-SP.png)
    * [Checkout](wireframes/Checkout-SP.png)

### Flowcharts
I used [Draw.io](https://app.diagrams.net/) to make a flowchart so I could get a better understanding of what happens when on the site for bothe the Admin User and Registered custom User.

![Flowchart](readme-images/meow-sweden-flowchart.png)

[Back to top](#table-of-content)

## Database Structure

### Category
**Name** | **Database Key** | **Field Type** | **Validation**
------------ | ------------- | ------------- | -------------
Name | name | CharField | max_length=200
Friendly Name | friendly_name | CharField | max_length=200, null=True, blank=True

### Products
**Name** | **Database Key** | **Field Type** | **Validation**
------------ | ------------- | ------------- | -------------
Category | category | ForeignKey | null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=200, null=True, blank=True
Name | name | CharField | max_length=200
Description | description | TextField| 
Cat ears has colors| catears_has_colors | BooleanField | default=False, null=True, blank=True
Quipu color| quipu_color | BooleanField | default=False, null=True, blank=True
Quipu stone pearl | quipu_stonepearl | BooleanField | default=False, null=True, blank=True
Price | price | DecimalField | max_digits=6, decimal_places=2
Image URL | image_url | URLField | max_length=1024, null=True, blank=True
Image | image | ImageField| null=True, blank=True


## Features
* Responsive on different devices
* Registration and log in for Customer Users
* Possability to edit Customer profile and view order history when logged in
* Browse products by category
* Possability for Admin User to add, edit and delete products when logged in

[Back to top](#table-of-content)


## Technologies Used
### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries 
* [Django](https://www.djangoproject.com/) was used for framework
* [Google Fonts](https://fonts.google.com/) was used to import the fonts mentioned above 
in the project
* [Coolors](https://coolors.co/) was used to decide on th colors and to create the color 
palette
* [Am I Responsive](http://ami.responsivedesign.is/) was used to make the mockup
* [Bootstrap](https://getbootstrap.com/) was used to make the site responsive
* [Font Awsome](https://fontawesome.com/) was used for the icons
* [Stripe](https://stripe.com/) was used to create payment infrastructure

### Tools
* [Balsamic](https://balsamiq.com) was used to create wireframes in the beginning of 
the project
* [Draw.io](https://app.diagrams.net/) was used to make the flowchart
* [Material.io](https://material.io/) was used to check that the contrast is ok
* [Gimp](https://www.gimp.org/) was used to edit photos.
* [Favicon.cc](https://www.favicon.cc/) was used to create the fave icon
* [Webformatter](https://webformatter.com/html) was used to beautify the code
??* [Copressor.io](https://compressor.io/) was used to compress the background image
* [Heroku](https://id.heroku.com/login) was used to deploy and host the site
* [Gitpod](https://gitpod.io/) was used for coding the project
* [Github](https://github.com/) was used to save and stored on the project after being 
pushed from Gitpod.
* [AWS S3 Bucket](https://aws.amazon.com/s3/) was used for storing static and media files

[Back to top](#table-of-content)


## Testing
You can read all about the testing of this site [Here](testing.md)

[Back to top](#table-of-content)


## Bugs

**Page content bug**
* **The main content of the pages is hidden underneith the main nav so the top of the page isn't visable**

Text

* **Fix**

Text

* **Verdict**

Text

**Name of bug**
* **Bug**

Text

* **Fix**

Text

* **Verdict**

Text

[Back to top](#table-of-content)


## To Do
* 
* 
* 

[Back to top](#table-of-content)


## Deployment
### GitHub Pages
How to deploy project using Github pages:

1. Go to Github
2. Log in and click on “Repositories” tab in the top middle of the screen
3. Choose this repository
4. Click on the "Settings" tab (with a gear icon)
5. Scroll down on the page until you find the "Github Pages" section
6. Under "Source" you'll find a dropdown which is set to "none"
7. Change it to "Master"
8. Then click the save button. This will reload the page.
9. Scroll back down to "Github Pages"
10. A green alert box will now tell you that your site been published and provide you a link to the site.

![Deployment Image](assets/images/deployment.png)

[Back to top](#table-of-content)

## Credits
#### Inspiration 
* [ ]( )
* [ ]( )

* Thank you to
* A huge thank you to my mentor Simen Eventyret_mentor for all the good advices, feedback 
and most of all patience.
* Thank you to my older brother David who’s been a wonderful support in me deepest times of 
dispear and helped me with testing and good advices to help me get a better understanding for the code.
You're the best!

[Back to top](#table-of-content)