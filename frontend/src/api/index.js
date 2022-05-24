export default async function apiCall({
  url,
  method= "get",
  body,
  headers= { 
    'Content-Type': 'application/json'
  }
}) {
  try {
    const response = await fetch(url, {
      method,
      body,
      headers
    });
  
    return response.json();
  } catch (error) {
    Promise.reject(error);
  }
}