from twotest.quicktest import QuickDjangoTest

if __name__ == '__main__':
    QuickDjangoTest(
        apps=("layers",),
        installed_apps=(
            'twotest',

        ),
        ROOT_URLCONF="",
        USE_TZ=True,
        STATIC_URL='/',
        LAYERS=dict(test='/static/test',
                    test2='/static/test2')
    )
