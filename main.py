# navigation_menu_generator.py

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive Navigation Menu</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <nav id="navbar">
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <div class="content">
        <h1>Welcome to the Page</h1>
        <p>Scroll down to see the navigation menu change!</p>
        <div style="height: 2000px;"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>


css_content = '''body {
    margin: 0;
    font-family: Arial, san-serif;
}

#navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background-color: #333;
    transition: background-color 0.3s ease;
    z-index: 1000;
}

#navbar.scrolled {
    background-color: #222;
}

#navbar ul {
    margin: 0;
   padding: 0;
    list-style: none;
    overflow: hidden;
    display: flex;
    justify-content: center;
}

#navbar li {
    float: left;
}

#navbar li a {
    display: block;
    padding: 20px 30px;
    color: white;
    text-decoration: none;
    transition: background-color 0.3s, color 0.3s;
}

#navbar li a:hover {
    background-color: #555;
    color: #ff0;
}

.content {
    margin-top: 80px;
    padding: 20px;
}
'''

js_content = '''window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
'''

# Create the files
with open('index.html', 'w') as html_file:
    html_file.write(html_content)

with open('style.css', 'w') as css_file:
    css_file.write(css_content)

with open('script.js', 'w') as js_file:
    js_file.write(js_content)

print("Files generated: index.html, style.css, script.js")
