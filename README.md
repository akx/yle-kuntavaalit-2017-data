# yle kuntavaalit 2017 data

# muni.json

Generated from https://vaalit.yle.fi/tulospalvelu/kv2017/kunnat with

```
JSON.stringify(
    Array.from(
        document.querySelectorAll('a.yed__municipality__index__item__link'))
        .map(a => ({name: a.innerText, link: a.href}))
        .map(l => ({name: l.name, data: /vaalipiiri\/(.+?)\/kunta\/(\d+)/.exec(l.link)}))
        .map(l => ({name: l.name, electorate: l.data[1], municipality: l.data[2]})
    )
)
```
