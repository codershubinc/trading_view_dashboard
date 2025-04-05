function toggleGraph() {
    const currentGraph =
        new URLSearchParams(window.location.search).get("graph") || "high";
    const newGraph = currentGraph === "high" ? "low" : "high";
    const url = new URL(window.location.href);
    url.searchParams.set("graph", newGraph);
    window.location.href = url;
}