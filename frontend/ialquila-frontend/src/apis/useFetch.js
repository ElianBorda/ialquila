import { useState, useEffect } from "react";

export function useFetch(url, numPage) {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(url)
            .then((res) => res.json())
            .then((data) => setData(data))
            // .catch(() => {})
    }, [url, numPage]);

    return { data }
}
