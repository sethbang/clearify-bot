from functions import clearify, get_modifier

MODELS = ["gpt-4-0314", "gpt-3.5-turbo", "gpt-3.5-turbo-16k-0613", "gpt-4-0613",
          "gpt-3.5-turbo-0301", "gpt-4", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-0613"]

comment = """Astronomer here! This has become a little more complex than the article indicates. The short answer is it turns out this spectral line for phosphine is really close to another one, for sulphur dioxide (which is much more common and prevalent in the universe). Some other teams analyzing the same data this original team used from the ALMA telescope in Chile argue the analysis was done wrong, and it wasn't phosphine but instead sulphur dioxide. There are now papers on why this second analysis is wrong, and it is indeed phosphine. Along the way, it turned out ALMA had a calibration pipeline error that also affected the data (basically Venus is SO BRIGHT the software didn't handle it as predicted), so it made the signal a little less robust, whatever it may be.

It is, in short, very clear that to lay this matter to rest they ought to do a better, longer observation with ALMA that minimizes effects from all the various issues. However, no team (be it the original or a rival team) have been awarded ALMA time since to try to observe phosphine again on Venus. (A lot of why is related to the astronomical politics of how telescope time is awarded, but the summary is way more people want to use ALMA than there are hours in the day to allocate.) So the team is doing what they can in the situation, and trying to identify the phosphine signal with other telescopes that aren't as good but can still detect it... and finding it! But if you're in the "misidentified sulphur dioxide line" camp, you're not gonna be convinced by this data either.

In conclusion, science is hard, spectral radio astronomy doubly so, but until the data quality is better we aren't going to know the truth for sure. It is a real shame though because it would be such a neat discovery if we could confirm it! Most people think Venus is a hellhole, but the upper atmosphere is actually really similar in temperature and pressure and all those things to Earth's, and the idea of some microorganisms floating around up there is certainly not an impossible one. But yeah, we just can't know for sure right now with the data we have."""


for each_model in MODELS:
    clear = clearify(comment, "layman", each_model)
    message = clear['choices'][0]['message']['content']
    with open(f"output/{each_model}.txt", "w") as f:
        f.write(message)
    print(f"Done with {each_model}")
