document.addEventListener("DOMContentLoaded", function () {
    const counter = document.querySelector(".counter-number"); // Fix: Select by class instead of id

    // Check if the element exists before updating it
    if (!counter) {
        console.error("Error: Counter element not found.");
        return;
    }

    async function updateCounter() {
        try {
            let response = await fetch(
                "https://zfnm62l55ess2bf7nmifbfcp5i0nzcjk.lambda-url.eu-north-1.on.aws/"
            );
            let data = await response.json();
            
            // Fix: Ensure correct JSON property access
            counter.innerHTML = `👀 Views: ${data.views || 0}`; 
        } catch (error) {
            console.error("Error fetching views:", error);
            counter.innerHTML = "Failed to load views";
        }
    }

    updateCounter();
});
