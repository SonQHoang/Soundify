import React, { createContext, useState } from 'react';

export const AuthContext = createContext(); // Creating new context for components to consume

export const AuthProvider = ({ children }) => { //AuthProvider uses the AuthContext.Provider to pass down auth state and the heper functions to children components
    const [isAuthenticated, setIsAuthenticated] = useState(true); // Auth initially set to true

    const logout = () => {
        setIsAuthenticated(false);
    }

    return ( // AuthContext.Provider allows for consuming components to subscribe to context changes. 
            // By passing isAuth, setIsAuth, and logout, any component that calls useContext(AuthContext) gets access
        <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated, logout }}>
            {children} 
        </AuthContext.Provider> // Children represents all of the components that I want to give the context access to
    );
};
