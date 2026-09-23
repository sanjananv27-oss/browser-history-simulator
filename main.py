history=[]


def visit_page(page):
    history.append(page)
    print("visited:",page)

def go_back(page):
    if history:
        page = history.pop()
        print("going back from:",page)
    else:
        print("no history available")

visit_page("google")
visit_page("youtube")
visit_page("instagram")

print("history:",history)

go_back("instagram")
go_back("youtube")


print("current history:",history)