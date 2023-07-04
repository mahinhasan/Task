# Base Project

This is a simple Django project that includes a blog, a portfolio, and a REST API.

## Blog

The blog app allows users to create and manage blog posts. Posts can be tagged and categorized, and they can be commented on by other users.

* To create a new blog post, users can go to the `/blog/new` URL.
* To edit an existing blog post, users can go to the `/blog/<post_id>/edit` URL, where `<post_id>` is the ID of the post to edit.
* To delete a blog post, users can go to the `/blog/<post_id>/delete` URL, where `<post_id>` is the ID of the post to delete.
* To view all blog posts, users can go to the `/blog` URL.
* To view blog posts tagged with a particular tag, users can go to the `/blog/tag/<tag>` URL, where `<tag>` is the name of the tag.
* To view blog posts categorized with a particular category, users can go to the `/blog/category/<category>` URL, where `<category>` is the name of the category.

## Portfolio

The portfolio app allows users to create and manage a portfolio of their work. Projects can be tagged and categorized, and they can be viewed by other users.

* To create a new project, users can go to the `/portfolio/new` URL.
* To edit an existing project, users can go to the `/portfolio/<project_id>/edit` URL, where `<project_id>` is the ID of the project to edit.
* To delete a project, users can go to the `/portfolio/<project_id>/delete` URL, where `<project_id>` is the ID of the project to delete.
* To view all projects, users can go to the `/portfolio` URL.
* To view projects tagged with a particular tag, users can go to the `/portfolio/tag/<tag>` URL, where `<tag>` is the name of the tag.
* To view projects categorized with a particular category, users can go to the `/portfolio/category/<category>` URL, where `<category>` is the name of the category.

## REST API

The REST API provides a way to interact with the data in the blog and portfolio apps. The API is documented using Swagger, and it can be accessed at `/api/docs`.

To use the REST API, you will need to use a tool like Postman or Insomnia. Once you have a tool, you can use it to send requests to the API endpoints. The API endpoints are documented in the Swagger documentation.

## Getting Started

To get started with this project, you will need to install the following dependencies:

* Python 3.8+
* Django 4.2+
* PostgreSQL

Once you have installed the dependencies, you can create a virtual environment and install the project's requirements by running the following commands:



# Base Project

This is a simple Django project that includes a blog, a portfolio, and a REST API.

## Blog

The blog app allows users to create and manage blog posts. Posts can be tagged and categorized, and they can be commented on by other users.

* To create a new blog post, users can go to the `/blog/new` URL.

    In the new blog post form, users will need to provide the following information:

    * Title
    * Content
    * Tags
    * Categories

    Once the user has submitted the form, the new blog post will be created and saved to the database.

* To edit an existing blog post, users can go to the `/blog/<post_id>/edit` URL, where `<post_id>` is the ID of the post to edit.

    In the edit blog post form, users will be able to see the current information for the post, and they can make changes to any of the fields. Once the user has saved the form, the changes will be saved to the database.

* To delete a blog post, users can go to the `/blog/<post_id>/delete` URL, where `<post_id>` is the ID of the post to delete.

    Once the user has confirmed that they want to delete the post, the post will be deleted from the database.

* To view all blog posts, users can go to the `/blog` URL.

    The blog page will display a list of all blog posts, with the most recent posts first. Each post will have a title, a summary of the content, and the date the post was published.

* To view blog posts tagged with a particular tag, users can go to the `/blog/tag/<tag>` URL, where `<tag>` is the name of the tag.

    The tag page will display a list of all blog posts that have been tagged with the specified tag.

* To view blog posts categorized with a particular category, users can go to the `/blog/category/<category>` URL, where `<category>` is the name of the category.

    The category page will display a list of all blog posts that have been categorized with the specified category.

## Portfolio

The portfolio app allows users to create and manage a portfolio of their work. Projects can be tagged and categorized, and they can be viewed by other users.

* To create a new project, users can go to the `/portfolio/new` URL.

    In the new project form, users will need to provide the following information:

    * Title
    * Description
    * Tags
    * Categories
    * Media (Image or Video)

    Once the user has submitted the form, the new project will be created and saved to the database.

* To edit an existing project, users can go to the `/portfolio/<project_id>/edit` URL, where `<project_id>` is the ID of the project to edit.

    In the edit project form, users will be able to see the current information for the project, and they can make changes to any of the fields. Once the user has saved the form, the changes will be saved to the database.

* To delete a project, users can go to the `/portfolio/<project_id>/delete` URL, where `<project_id>` is the ID of the project to delete.

    Once the user has confirmed that they want to delete the project, the project will be deleted from the database.

* To view all projects, users can go to the `/portfolio` URL.

    The portfolio page will display a list of all projects, with the most recent projects first. Each project will have a title, a summary of the project, and the date the project was created.

* To view projects tagged with a particular tag, users can go to the `/portfolio/tag/<tag>` URL, where `<tag>` is the name of the tag.

    The tag page will display a list of all projects that have been tagged with the specified tag.

* To view projects categorized with a particular category, users can go to the `/portfolio/category/<category>` URL, where `<category>` is the name of the category.

    The category page will display a list of all projects that have been categorized with the specified category.

## REST API
