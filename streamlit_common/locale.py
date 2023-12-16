def get_locale():
    return {
        "search": {
            "title": {"en": "Card Search", "ja": "カード検索"},
            "instructions": {
                "en": "Enter any English or Japanese text to find all [Middle School legal](https://www.eternalcentral.com/middleschoolrules/) card titles which include it.",
                "ja": "カードの英語名か日本語名を入力し始めると[ミドルスクールで使用可能](https://www.eternalcentral.com/middleschoolrules/)なカード名が引っかかります。",
            },
            "cards_are_legal": {
                "en": " cards are legal.",
                "ja": "枚 のカードが使用可能です。",
            },
            "search_by_card_name": {
                "en": "Search by card name:",
                "ja": "カード名で検索：",
            },
            "search_by_card_name_placeholder": {
                "en": "Type a card name or part of it",
                "ja": "カード名もしくはその一部を入力してください",
            },
            "select_type": {
                "en": "Select card type:",
                "ja": "タイプを選択してください：",
            },
            "search_by_type": {
                "en": "Search by card type:",
                "ja": "カードタイプで検索：",
            },
            "search_by_type_placeholder": {
                "en": "Type a type, subtype or supertype",
                "ja": "タイプ、サブタイプ、スーパータイプを入力",
            },
            "select_type_placeholder": {
                "en": "Select card type(s)",
                "ja": "カードタイプ選択",
            },
            "search_by_text": {
                "en": "Search by rules text:",
                "ja": "テキストで検索：",
            },
            "search_by_text_placeholder": {
                "en": "Type a part of the rules text",
                "ja": "テキストの一部を入力してください",
            },
            "exact_match": {
                "en": "is an exact match.",
                "ja": "が完全一致します。",
            },
            "search_by_color": {
                "en": "Color:",
                "ja": "色：",
            },
            "search_by_mv": {
                "en": "Mana value:",
                "ja": "マナ総量：",
            },
            "search_by_pow": {
                "en": "Power:",
                "ja": "パワー：",
            },
            "search_by_tou": {
                "en": "Toughness:",
                "ja": "タフネス：",
            },
            "cards_found": {
                "en": " cards were found.",
                "ja": "枚 のカードが見つかりました。",
            },
            "top_results": {
                "en": "Top results:",
                "ja": "上位の検索結果：",
            },
            "see_more": {
                "en": "See more results",
                "ja": "さらに表示する",
            },
            "see_20": {
                "en": "Reset to 20 results",
                "ja": "上位20枚表示に戻す",
            },
        },
        "check": {
            "title": {
                "en": "List Check",
                "ja": "リストチェック",
            },
            "instructions": {
                "en": "Paste or type your list here to confirm that every card in it is [Middle School legal](https://www.eternalcentral.com/middleschoolrules/).",
                "ja": "[ミドルスクールで使用可能](https://www.eternalcentral.com/middleschoolrules/)かどうかを確認するには、ここにリストを貼り付けたり入力したりしてください。",
            },
            "card_list": {
                "en": "Card list",
                "ja": "カードリスト",
            },
            "illegal_cards_1": {
                "en": "**",
                "ja": "使用不可カード **",
            },
            "illegal_cards_2": {
                "en": "** illegal cards",
                "ja": "**枚",
            },
        },
        "basic": {
            "color_w": {
                "en": "W",
                "ja": "白",
            },
            "color_u": {
                "en": "U",
                "ja": "青",
            },
            "color_b": {
                "en": "B",
                "ja": "黒",
            },
            "color_r": {
                "en": "R",
                "ja": "赤",
            },
            "color_g": {
                "en": "G",
                "ja": "緑",
            },
            "color_c": {
                "en": "C",
                "ja": "無/茶",
            },
            "type_artifact": {
                "en": "Artifact",
                "ja": "アーティファクト",
            },
            "type_creature": {
                "en": "Creature",
                "ja": "クリーチャー",
            },
            "type_enchantment": {
                "en": "Enchantment",
                "ja": "エンチャント",
            },
            "type_instant": {
                "en": "Instant",
                "ja": "インスタント",
            },
            "type_land": {
                "en": "Land",
                "ja": "土地",
            },
            "type_sorcery": {
                "en": "Sorcery",
                "ja": "ソーサリー",
            },
        },
    }


def get_type_options():
    _ = get_locale()
    return {
        "en": [
            _["basic"]["type_artifact"]["en"],
            _["basic"]["type_creature"]["en"],
            _["basic"]["type_enchantment"]["en"],
            _["basic"]["type_instant"]["en"],
            _["basic"]["type_land"]["en"],
            _["basic"]["type_sorcery"]["en"],
        ],
        "ja": [
            _["basic"]["type_artifact"]["ja"],
            _["basic"]["type_creature"]["ja"],
            _["basic"]["type_enchantment"]["ja"],
            _["basic"]["type_instant"]["ja"],
            _["basic"]["type_land"]["ja"],
            _["basic"]["type_sorcery"]["ja"],
        ],
    }
