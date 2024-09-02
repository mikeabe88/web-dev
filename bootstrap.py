from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bootstrap Class Codes', 0, 1, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.chapter_title('General Structure')

# General Structure content
general_structure = """
Containers:
<div class="container">...</div>
<div class="container-fluid">...</div>

Grid System:
<div class="row">
    <div class="col">...</div>
    <div class="col">...</div>
</div>

Specific column sizes:
<div class="col-4">...</div>
<div class="col-md-6">...</div>
"""
pdf.chapter_body(general_structure)

# Set Typography
pdf.chapter_title('Typography')

# Typography content
typography = """
Headings:
<h1 class="display-1">...</h1>
<h2 class="display-2">...</h2>

Text Utilities:
<p class="text-primary">...</p>
<p class="text-secondary">...</p>
<p class="text-success">...</p>
<p class="text-danger">...</p>
<p class="text-warning">...</p>
<p class="text-info">...</p>
<p class="text-light bg-dark">...</p>
<p class="text-dark">...</p>
<p class="text-muted">...</p>
<p class="text-white bg-dark">...</p>

Text Alignment:
<p class="text-left">...</p>
<p class="text-center">...</p>
<p class="text-right">...</p>

Text Transformation:
<p class="text-lowercase">...</p>
<p class="text-uppercase">...</p>
<p class="text-capitalize">...</p>
"""
pdf.chapter_body(typography)

# Set Colors and Backgrounds
pdf.chapter_title('Colors and Backgrounds')

# Colors and Backgrounds content
colors_backgrounds = """
Background Color:
<div class="bg-primary">...</div>
<div class="bg-secondary">...</div>
<div class="bg-success">...</div>
<div class="bg-danger">...</div>
<div class="bg-warning">...</div>
<div class="bg-info">...</div>
<div class="bg-light">...</div>
<div class="bg-dark">...</div>
<div class="bg-white">...</div>
"""
pdf.chapter_body(colors_backgrounds)

# Set Buttons
pdf.chapter_title('Buttons')

# Buttons content
buttons = """
Button Styles:
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-light">Light</button>
<button class="btn btn-dark">Dark</button>
<button class="btn btn-link">Link</button>

Button Sizes:
<button class="btn btn-primary btn-lg">Large button</button>
<button class="btn btn-primary btn-sm">Small button</button>

Block Button:
<button class="btn btn-primary btn-block">Block level button</button>
"""
pdf.chapter_body(buttons)

# Set Forms
pdf.chapter_title('Forms')

# Forms content
forms = """
Form Elements:
<form>
    <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    </div>
    <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>

Form Layouts:
<div class="form-row">
    <div class="form-group col-md-6">
        <label for="inputEmail4">Email</label>
        <input type="email" class="form-control" id="inputEmail4" placeholder="Email">
    </div>
    <div class="form-group col-md-6">
        <label for="inputPassword4">Password</label>
        <input type="password" class="form-control" id="inputPassword4" placeholder="Password">
    </div>
</div>
"""
pdf.chapter_body(forms)

# Set Cards
pdf.chapter_title('Cards')

# Cards content
cards = """
Basic Card:
<div class="card" style="width: 18rem;">
    <img class="card-img-top" src="..." alt="Card image cap">
    <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>

Card Groups:
<div class="card-group">
    <div class="card">
        <img class="card-img-top" src="..." alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        </div>
    </div>
    <div class="card">
        <img class="card-img-top" src="..." alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
        </div>
    </div>
</div>
"""
pdf.chapter_body(cards)

# Set Utilities
pdf.chapter_title('Utilities')

# Utilities content
utilities = """
Spacing:
<div class="mt-3">Margin top 3</div>
<div class="mb-3">Margin bottom 3</div>
<div class="ml-3">Margin left 3</div>
<div class="mr-3">Margin right 3</div>
<div class="p-3">Padding 3</div>

Display Property:
<div class="d-none">Hidden</div>
<div class="d-inline">Inline</div>
<div class="d-block">Block</div>
<div class="d-flex">Flex</div>

Flex Utilities:
<div class="d-flex justify-content-start">...</div>
<div class="d-flex justify-content-center">...</div>
<div class="d-flex justify-content-end">...</div>
<div class="d-flex justify-content-around">...</div>
<div class="d-flex justify-content-between">...</div>
"""
pdf.chapter_body(utilities)

# Set Tables
pdf.chapter_title('Tables')

# Tables content
tables = """
Basic Table:
<table class="table">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
        </tr>
    </tbody>
</table>

Table Variants:
<table class="table table-striped">...</table>
<table class="table table-bordered">...</table>
<table class="table table-hover">...</table>
<table class="table table-sm">...</table>
"""
pdf.chapter_body(tables)

# Set Modals
pdf.chapter_title('Modals')

# Modals content
modals = """
Basic Modal:
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                ...
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
        </div>
    </div>
</div>
"""
pdf.chapter_body(modals)

# Set Alerts
pdf.chapter_title('Alerts')

# Alerts content
alerts = """
Basic Alert:
<div class="alert alert-primary" role="alert">
    This is a primary alert—check it out!
</div>
"""
pdf.chapter_body(alerts)

# Save PDF to file
pdf_file_path = D:\LG drive\ROGER\WEB DEV
