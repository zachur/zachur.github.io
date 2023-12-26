def create_webpage(doctype_file, \
                 head_file, \
                 header_file, \
                 main_file, \
                 footer_file, \
                 output_file):
    try:
        with open(doctype_file, 'r') as f:
            doctype_content = f.read()

        with open(head_file, 'r') as f:
            head_content = f.read()

        with open(header_file, 'r') as f:
            header_content = f.read()

        with open(main_file, 'r') as f:
            main_content = f.read()

        with open(footer_file, 'r') as f:
            footer_content = f.read()

        combined_document = f"{doctype_content}\n{head_content}\n{header_content}\n{main_content}\n{footer_content}"

        with open(output_file, 'w') as f:
            f.write(combined_document)

        print(f"Webpage created: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

create_webpage("../html/doctype.html", \
             "../html/head.html", \
             "../html/header.html", \
             "../html/homepage.html", \
             "../html/footer.html", \
             "../../index.html")
