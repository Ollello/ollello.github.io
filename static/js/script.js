document.addEventListener('DOMContentLoaded', () => {
    const content = document.getElementById('content');
    const nav = document.querySelector('nav');

    nav.addEventListener('click', (e) => {
        if (e.target.tagName === 'A') {
            e.preventDefault();
            const url = e.target.href;
            navigateTo(url);
        }
    });

    content.addEventListener('click', (e) => {
        if (e.target.classList.contains('read-more') || e.target.classList.contains('back-link')) {
            e.preventDefault();
            const url = e.target.href;
            navigateTo(url);
        }
    });

    window.addEventListener('popstate', (e) => {
        if (e.state) {
            content.innerHTML = e.state.html;
        }
    });

    async function navigateTo(url) {
        content.classList.add('loading');
        try {
            const response = await fetch(url);
            const html = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const newContent = doc.querySelector('#content').innerHTML;
            content.innerHTML = newContent;
            history.pushState({ html: newContent }, '', url);
        } catch (error) {
            console.error('Navigation error:', error);
        } finally {
            content.classList.remove('loading');
        }
    }
});

console.log('Script loaded');
