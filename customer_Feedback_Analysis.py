###Customer Feedback Analysis 6
def positive_feedback(ratings):
  if not ratings:
    return "There are no ratings"
  else:
    positivecount=0
    for i in ratings:
      if i>=4:
        positivecount=positivecount+1
    percent=(positivecount/len(ratings))*100
    return f"Positive Feedback: {percent:.1f}%"     


ratings=eval(input("ratings = "))
res=positive_feedback(ratings)
print(res)
