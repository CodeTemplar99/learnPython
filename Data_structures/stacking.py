# stacking is a method of piling up items or objects, in real life it's more like the
# organization of browsing history or web pages visited on a tab.
# this process uses a method known by the acronym LIFO - last in, first out
# to implement this in python we can do this

# define an empty browsing session list
browsing_session = []
# add an item/visit a page
browsing_session.append(1)
# remove the last item/press the back button
browsing_session.pop()

# check if our session is empty(to disable back button)
if not browsing_session:
  # use negative index to get the last item in the stack
    browsing_session[-1]
