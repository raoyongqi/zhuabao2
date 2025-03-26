// const customElement = document.querySelectorAll('ng-star-inserted');

// // 检查 shadowRoot 是否可访问
// if (customElement.shadowRoot) {
//   console.log('This is an Open Mode Shadow DOM');
// } else {
//   console.log('This is a Closed Mode Shadow DOM');
// }
const links = Array.from(document.querySelectorAll('.ng-star-inserted'));
const filteredLinks = links.filter(link => !link.hasAttribute('style'));
function findHref(element) {
    // 如果元素为空，返回 null
    if (!element) return null;
    const secondElement = element.children[1]; // 第二个子元素的索引是 1

    if (!secondElement) return null;
    const firstChildOfSecondElement = secondElement ? secondElement.children[1] : null;

    if (firstChildOfSecondElement && firstChildOfSecondElement.href) {
        return element; // Return the href value instead of the element
    }

    return null;
}

let foundCount = 0;

for (let link of filteredLinks) {
    const href = findHref(link);

    if (href) {
        foundCount++;  // Increment the found count

        // 如果找到第二个符合条件的链接，则跳出循环并在新窗口打开链接
        if (foundCount === 2) {
            console.log(href.shadowRoot); // 打印找到的 href 属性
            break; // Stop the loop after opening the second link
        }
    } else {
        console.log("第二个子元素或其子元素没有 href 属性");
    }
}