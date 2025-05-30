
import pandas as pd
data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

import altair as alt
chart = alt.Chart(data)

chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
print(chart.to_json())

chart.save("../chart.html", embed_options={'renderer': 'svg'})
chart.save("../chart.svg")
