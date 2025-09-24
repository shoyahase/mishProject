


// テキストを表示するコンテナ
const textContainer = document.getElementById('text-container');

// Djangoから渡されたテキストデータを取得
const correctText = textContainer.dataset.correctText;

// メッセージ表示用のコンテナ
const resultMessage = document.getElementById('result-message');

// 現在の入力位置を示すインデックス
let currentIndex = 0;

// 完了メッセージを表示する代わりに、フォームを操作する
const resultForm = document.getElementById('result-form');
const userInputField = document.getElementById('user-input-field');

// ユーザーが入力した文字を保存する配列
const userInputArray = [];

// テキストを一文字ずつ<span>要素に分解してコンテナに追加
// "text" → <span>t<\span>
const textSpans = correctText.split('').map(char => {
    const span = document.createElement('span');
    span.textContent = char;
    textContainer.appendChild(span);
    return span;
});

// 最初の文字にカーソルを合わせる
if (textSpans.length > 0) {
    textSpans[currentIndex].classList.add('cursor');
}

// キー入力のイベントを監視
// 何かのキーが押されたら以下が実行される
document.addEventListener('keydown', (event) => {
    // すべて打ち終わったら何もしない
    if (currentIndex >= correctText.length) {
        return;
    }

    // 入力されたキー
    const typedChar = event.key;
    
    // 現在の正解文字のspan要素
    const currentSpan = textSpans[currentIndex];
    
    // 期待される文字
    const expectedChar = correctText[currentIndex];

    // Backspaceキーの処理
    if (typedChar === 'Backspace') {
        if (currentIndex > 0) {
            // カーソルを一つ前に戻す
            currentSpan.classList.remove('cursor');
            currentIndex--;
            // 前の文字のスタイルをリセットし、カーソルを当てる
            textSpans[currentIndex].classList.remove('correct', 'incorrect');
            textSpans[currentIndex].classList.add('cursor');

            // ★★★ 配列からも最後の文字を削除する ★★★
            userInputArray.pop();
        }
        return; // Backspace処理後は終了
    }

    // 通常の文字キーか、Shiftなどの特殊キーかを判定 (1文字のキーのみを対象)
    if (typedChar.length !== 1) {
        return;
    }

    // 正誤判定
    if (typedChar === expectedChar) {
        currentSpan.classList.add('correct');
        currentSpan.classList.remove('incorrect');

        userInputArray[currentIndex] = typedChar;
    } else {
        currentSpan.classList.add('incorrect');
        currentSpan.classList.remove('correct');

        userInputArray[currentIndex] = typedChar;

    }

    // カーソルを次に進める
    currentSpan.classList.remove('cursor');
    currentIndex++;

    // 全ての文字を打ち終わったかチェック
    if (currentIndex < correctText.length) {
        textSpans[currentIndex].classList.add('cursor');
    } else {
        const finalUserInput = userInputArray.join('');
    
        // 非表示のinput要素に、完成した文字列を値として設定
        userInputField.value = finalUserInput;

        // 完了メッセージを表示
        resultMessage.style.display = 'block';
    }
});