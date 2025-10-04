// 表示用テキストの準備
const textContainer = document.getElementById('text-container');
const hiraganaText = textContainer.dataset.correctText;
const textSpans = hiraganaText.split('').map(char => {
    const span = document.createElement('span');
    span.textContent = char;
    textContainer.appendChild(span);
    return span;
});

// フォーム関連の要素を取得
const userInputArea = document.getElementById('user-input-area'); // ★ forms.pyで指定したID
const submitButton = document.getElementById('submit-button');

// ★★★ テキストエリアのinputイベントを監視 ★★★
userInputArea.addEventListener('input', () => {
    // 入力欄に入っている現在のテキストを取得
    const typedText = userInputArea.value;
    
    // 表示されているテキスト（span）の色を更新する
    textSpans.forEach((charSpan, index) => {
        const typedChar = typedText[index];

        // 未入力の文字はスタイルをリセット
        if (typedChar === undefined) {
            charSpan.classList.remove('correct', 'incorrect', 'cursor');
            return;
        }
        
        // 正誤を判定して色付け
        if (typedChar === charSpan.textContent) {
            charSpan.classList.add('correct');
            charSpan.classList.remove('incorrect');
        } else {
            charSpan.classList.add('incorrect');
            charSpan.classList.remove('correct');
        }
    });

    // カーソル位置を更新
    const currentIndex = typedText.length;
    textSpans.forEach(span => span.classList.remove('cursor'));
    if (currentIndex < textSpans.length) {
        textSpans[currentIndex].classList.add('cursor');
    }

    // 全ての文字を入力し終えたかチェック
    if (typedText.length >= hiraganaText.length) {
        submitButton.style.display = 'inline-block'; // 採点ボタンを表示
    } else {
        submitButton.style.display = 'none'; // まだ途中なら隠す
    }
});

// 最初の文字にカーソルを合わせる
if (textSpans.length > 0) {
    textSpans[0].classList.add('cursor');
}