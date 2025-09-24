// ひらがな・ローマ字対応表
const hiraganaToRoman = {
    'あ': ['a'], 'い': ['i'], 'う': ['u'], 'え': ['e'], 'お': ['o'],
    'か': ['ka'], 'き': ['ki'], 'く': ['ku'], 'け': ['ke'], 'こ': ['ko'],
    'さ': ['sa'], 'し': ['shi', 'si'], 'す': ['su'], 'せ': ['se'], 'そ': ['so'],
    'た': ['ta'], 'ち': ['chi', 'ti'], 'つ': ['tsu', 'tu'], 'て': ['te'], 'と': ['to'],
    'な': ['na'], 'に': ['ni'], 'ぬ': ['nu'], 'ね': ['ne'], 'の': ['no'],
    'は': ['ha'], 'ひ': ['hi'], 'ふ': ['fu', 'hu'], 'へ': ['he'], 'ほ': ['ho'],
    'ま': ['ma'], 'み': ['mi'], 'む': ['mu'], 'め': ['me'], 'も': ['mo'],
    'や': ['ya'], 'ゆ': ['yu'], 'よ': ['yo'],
    'ら': ['ra'], 'り': ['ri'], 'る': ['ru'], 'れ': ['re'], 'ろ': ['ro'],
    'わ': ['wa'], 'を': ['wo'], 'ん': ['n', 'nn', "n'"],
    'が': ['ga'], 'ぎ': ['gi'], 'ぐ': ['gu'], 'げ': ['ge'], 'ご': ['go'],
    'ざ': ['za'], 'じ': ['ji', 'zi'], 'ず': ['zu'], 'ぜ': ['ze'], 'ぞ': ['zo'],
    'だ': ['da'], 'ぢ': ['di'], 'づ': ['du'], 'で': ['de'], 'ど': ['do'],
    'ば': ['ba'], 'び': ['bi'], 'ぶ': ['bu'], 'べ': ['be'], 'ぼ': ['bo'],
    'ぱ': ['pa'], 'ぴ': ['pi'], 'ぷ': ['pu'], 'ぺ': ['pe'], 'ぽ': ['po'],

    'きゃ': ['kya'], 'きゅ': ['kyu'], 'きょ': ['kyo'],
    'しゃ': ['sha', 'sya'], 'しゅ': ['shu', 'syu'], 'しょ': ['sho', 'syo'],
    'ちゃ': ['cha', 'tya'], 'ちゅ': ['chu', 'tyu'], 'ちょ': ['cho', 'tyo'],
    'にゃ': ['nya'], 'にゅ': ['nyu'], 'にょ': ['nyo'],
    'ひゃ': ['hya'], 'ひゅ': ['hyu'], 'ひょ': ['hyo'],
    'みゃ': ['mya'], 'みゅ': ['myu'], 'みょ': ['myo'],
    'りゃ': ['rya'], 'りゅ': ['ryu'], 'りょ': ['ryo'],
    'ぎゃ': ['gya'], 'ぎゅ': ['gyu'], 'ぎょ': ['gyo'],
    'じゃ': ['ja', 'zya'], 'じゅ': ['ju', 'zyu'], 'じょ': ['jo', 'zyo'],
    'ぢゃ': ['dya'], 'ぢゅ': ['dyu'], 'ぢょ': ['dyo'],
    'びゃ': ['bya'], 'びゅ': ['byu'], 'びょ': ['byo'],
    'ぴゃ': ['pya'], 'ぴゅ': ['pyu'], 'ぴょ': ['pyo'],

    'うぁ': ['wha'], 'うぃ': ['wi'], 'うぇ': ['we', 'whe'], 'うぉ': ['who'],
    'くぁ': ['qa', 'kwa'], 'くぃ': ['qi'], 'くぇ': ['qe'], 'くぉ': ['qo'],
    'ぐぁ': ['gwa'],
    'つぁ': ['tsa'], 'つぃ': ['tsi'], 'つぇ': ['tse'], 'つぉ': ['tso'],
    'てゃ': ['tha'], 'てぃ': ['thi'], 'てゅ': ['thu'],
    'でゃ': ['dha'], 'でぃ': ['dhi'], 'でゅ': ['dhu'],
    'とぁ': ['twa'], 'とぃ': ['twi'], 'とぅ': ['twu'], 'とぇ': ['twe'], 'とぉ': ['two'],
    'ふぁ': ['fa'], 'ふぃ': ['fi'], 'ふぇ': ['fe'], 'ふぉ': ['fo'],
    'ふゃ': ['fya'], 'ふゅ': ['fyu'], 'ふょ': ['fyo'],
    
    'いぇ': ['ye'],

    'ー': ['-'], '、': [','], '。': ['.'], '・': ['/'],
    'ぁ': ['xa'], 'ぃ': ['xi'], 'ぅ': ['xu'], 'ぇ': ['xe'], 'ぉ': ['xo'],
    'ゃ': ['xya'], 'ゅ': ['xyu'], 'ょ': ['xyo'],
    'っ': ['xtu'], // 促音は特別処理が必要
};

/**
 * ひらがな/カタカナの文字列をローマ字に変換する関数
 * @param {string} text 変換したい文字列
 * @returns {string} 変換後のローマ字文字列
 */
function convertToRoman(text) {
    let romanText = '';
    for (let i = 0; i < text.length; i++) {
        // 2文字の拗音（「きゃ」など）を先にチェック
        if (i + 1 < text.length && hiraganaToRoman[text.substring(i, i + 2)]) {
            romanText += hiraganaToRoman[text.substring(i, i + 2)];
            i++; // 2文字分進める
        } 
        // 促音（「っ」）の処理
        else if (text[i] === 'っ') {
            // 次の文字の子音を重ねる
            if (i + 1 < text.length) {
                const nextCharRoman = hiraganaToRoman[text[i + 1]];
                if (nextCharRoman) {
                    romanText += nextCharRoman.charAt(0);
                }
            }
        }
        // 1文字のひらがな
        else if (hiraganaToRoman[text[i]]) {
            romanText += hiraganaToRoman[text[i]];
        }
        // 対応表にない文字はそのまま追加
        else {
            romanText += text[i];
        }
    }
    return romanText;
}

/**
 * ひらがな文字列をタイピングの単位（「か」や「きゃ」など）に分解する
 * @param {string} text 分解したい文字列
 * @returns {string[]} 分解後の単位の配列
 */
function parseToTypingUnits(text) {
    const units = [];
    for (let i = 0; i < text.length; i++) {
        // 2文字の拗音などを先にチェック
        const twoCharUnit = text.substring(i, i + 2);
        if (hiraganaToRoman[twoCharUnit]) {
            units.push(twoCharUnit);
            i++; // 2文字分進める
        } else {
            units.push(text[i]);
        }
    }
    return units;
}


// テキストを表示するコンテナ
const textContainer = document.getElementById('text-container');
// Djangoから渡されたテキストデータを取得
const hiraganaText = textContainer.dataset.correctText;

// ★★★ タイピング単位の配列を作成 ★★★
const hiraganaUnits = parseToTypingUnits(hiraganaText);
// ★★★ 判定に使うローマ字文を生成 ★★★
const correctText = hiraganaUnits.map(unit => convertToRoman(unit)).join('');

console.log("hiraganaUnits",hiraganaUnits);
console.log("correctText", correctText);

// メッセージ表示用のコンテナ
const resultMessage = document.getElementById('result-message');

// 現在の入力位置を示すインデックス
let romanIndex = 0;
let hiraganaUnitIndex = 0;

// 完了メッセージを表示する代わりに、フォームを操作する
const resultForm = document.getElementById('result-form');
const userInputField = document.getElementById('user-input-field');

// ユーザーが入力した文字を保存する配列
const userInputArray = [];

// テキストを一文字ずつ<span>要素に分解してコンテナに追加
// "text" → <span>t<\span>
const textSpans = hiraganaUnits.map(unit => { // unit には 'きょ', 'う' が順番に入る
    const span = document.createElement('span');
    span.textContent = unit;
    textContainer.appendChild(span);
    return span;
});

// 最初の平仮名にカーソルを合わせる
if (textSpans.length > 0) {
    textSpans[hiraganaUnitIndex].classList.add('cursor');
}


let typedForCurrentUnit = ''; // ★★★ 現在の単位に対して入力されたローマ字を保持する変数 ★★★

// キー入力のイベントを監視
// 何かのキーが押されたら以下が実行される
document.addEventListener('keydown', (event) => {
    if (romanIndex >= correctText.length) {
        return;
    }

    const typedChar = event.key;
    if (typedChar.length !== 1) { // Backspaceなどは一旦無視
        return;
    }

    const currentUnit = hiraganaUnits[hiraganaUnitIndex];
    const currentUnitSpan = textSpans[hiraganaUnitIndex];

    // ★★★ 新しい判定ロジック ★★★

    // 1. 正解となるローマ字のパターンを全て取得
    let possibleRomans = hiraganaToRoman[currentUnit] || [currentUnit];
    if (!Array.isArray(possibleRomans)) {
        possibleRomans = [possibleRomans]; // 配列でない場合は配列に変換
    }

    // 2. 今回の入力を含めた、現在の単位の入力文字列を作成
    const newTyped = typedForCurrentUnit + typedChar;

    // 3. 入力文字列が、いずれかの正解パターンの「途中」と一致するかチェック
    const isPrefix = possibleRomans.some(roman => roman.startsWith(newTyped));
    
    // 4. 入力文字列が、いずれかの正解パターンと「完全に」一致するかチェック
    const isComplete = possibleRomans.includes(newTyped);

    if (isComplete) {
        // --- 完全に一致した場合（単位の入力完了） ---
        currentUnitSpan.classList.add('correct');
        currentUnitSpan.classList.remove('cursor');
        hiraganaUnitIndex++; // 次の単位へ
        typedForCurrentUnit = ''; // 現在の単位の入力をリセット

        if (hiraganaUnitIndex < hiraganaUnits.length) {
            textSpans[hiraganaUnitIndex].classList.add('cursor');
        }

    } else if (isPrefix) {
        // --- 途中の場合（まだ入力が続く） ---
        typedForCurrentUnit = newTyped;

    } else {
        // --- 間違っている場合 ---
        textContainer.classList.add('shake');
        setTimeout(() => textContainer.classList.remove('shake'), 200);
        return;
    }


    // --- 終了判定 ---
    if (hiraganaUnitIndex >= hiraganaUnits.length) {
        // 完了処理 (ユーザーが実際に入力した内容を送信するロジックは別途必要)
        resultForm.style.display = 'block';
    }
});
