// User Store 

// User Store
// Path: frontend/src/store/user.ts
// Compare this snippet from frontend/src/store/auth.ts:
//

import { computed } from 'vue';
import { defineStore } from 'pinia';
import { useAuth0 } from '@auth0/auth0-vue';
import type { User } from '@auth0/auth0-spa-js';

