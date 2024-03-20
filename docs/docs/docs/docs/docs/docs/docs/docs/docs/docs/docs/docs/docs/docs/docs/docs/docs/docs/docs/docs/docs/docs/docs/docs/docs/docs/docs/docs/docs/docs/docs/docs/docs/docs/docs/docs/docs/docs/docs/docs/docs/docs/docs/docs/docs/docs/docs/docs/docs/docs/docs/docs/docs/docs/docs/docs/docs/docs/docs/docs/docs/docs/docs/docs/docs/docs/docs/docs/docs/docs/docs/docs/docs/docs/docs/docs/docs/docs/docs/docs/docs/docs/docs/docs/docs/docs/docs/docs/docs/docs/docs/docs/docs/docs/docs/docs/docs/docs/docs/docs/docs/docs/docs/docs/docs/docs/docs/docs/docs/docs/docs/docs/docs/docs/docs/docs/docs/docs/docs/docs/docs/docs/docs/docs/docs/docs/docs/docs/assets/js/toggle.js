function showMore(buttonElement) {
    const contentDiv = buttonElement.nextElementSibling;

    if (contentDiv && contentDiv.classList.contains("hidden-content")) {
        contentDiv.style.display = "block";
        buttonElement.style.display = "none";
        
        // hideボタンの参照を取得して表示します
        const hideButton = contentDiv.querySelector('button[onclick="hideContent(this)"]');
        if (hideButton) {
            hideButton.style.display = "block";
        }
    }
}

function hideContent(buttonElement) {
    const contentDiv = buttonElement.parentNode;

    if (contentDiv && contentDiv.classList.contains("hidden-content")) {
        contentDiv.style.display = "none";
        
        // moreボタンの参照を取得して表示します
        const moreButton = contentDiv.previousElementSibling;
        if (moreButton) {
            moreButton.style.display = "block";
        }
        
        buttonElement.style.display = "none"; // hideボタンを隠します
    }
}
