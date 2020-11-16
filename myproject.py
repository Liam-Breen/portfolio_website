from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/")
def render_home_page():
    return render_template('home.html')

@app.route("/projects")
def render_projects():
    github_info = get_github_info()
    return render_template('projects.html', github_info=github_info)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/success")
def success():
    return render_template('success.html')


def get_github_info():

    github_username = "Liam-Breen"
    main_page_url = f"https://github.com/{github_username}?tab=repositories"
    main_page = requests.get(url = main_page_url)
    main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
    repos = main_page_soup.find_all("a", itemprop="name codeRepository")

    github_info = []
    for repo in repos:

        repo_info = {}

        repo_url = f"https://github.com/{github_username}/{repo.text.strip()}"
        repo_info['repo_url'] = repo_url
        repo_page = requests.get(url = repo_url)
        repo_page_soup = BeautifulSoup(repo_page.content, 'html.parser')

        title = repo_page_soup.find("meta", {"property":"og:title"})['content']
        title = title.split('/')[1]
        repo_info['title'] = title

        desc_content = repo_page_soup.find("meta", {"name":"description"})['content']
        # This is needed add the end of your description to create the tags section
        desc_content_split = desc_content.split('END')
        description = desc_content_split[0]
        repo_info['description'] = description
        tags = desc_content_split[1]
        repo_info['tags'] = tags

        github_info.append(repo_info)


    return github_info

if __name__ == "__main__":
    app.run(host='127.0.0.1')


