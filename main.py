import sys
import panflute

headers = dict()

def upper_str(element, _):
    if isinstance(element, panflute.Str):
        element.text = element.text.upper()

def my_filter(element, _):
    if isinstance(element, panflute.Header) and element.level <= 3:
        return element.walk(upper_str)
    if isinstance(element, panflute.Str) and element.text.lower() == "bold":
        return panflute.Strong(element)
    if isinstance(element, panflute.Header):
        text = panflute.stringify(element)
        if text in headers.keys():  
            if not headers[text]: 
                sys.stderr.write(f"Header repeated: \"{text}\"")
                headers[text] = True
        else:
            headers[text] = False

def main(doc=None):
    return panflute.run_filter(my_filter, doc=doc)


if __name__ == "__main__":
    main()
