import { spyOn } from "@vitest/spy";
import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import Login from '../Login.vue';

describe('user login - check input email', () => {
  it ('starts with no email error', () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    });
    expect(wrapper.vm.errors.credentials.email).toBe(false);
  });

  it ('email error true when empty', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.email).toBe(true);
  });

  it ('email error false when have @', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: 'jkahvedjian@gmail.com',
          password: ''
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.email).toBe(false);
  });

  it('email error true when does not have @', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: 'jkahvedjian',
          password: ''
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.email).toBe(true);
  });
});

describe('user login - check input password', () => {
  it ('starts with no password error', () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    });
    expect(wrapper.vm.errors.credentials.password).toBe(false);
  });

  it ('password error true when empty', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.password).toBe(true);
  });

  it ('password error false when have 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '12345678'
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.password).toBe(false);
  });

  it ('password error false when have more then 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '123456789'
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.password).toBe(false);
  });

  it('password error true when have less then 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '1234567'
        }
      }
    });
    await wrapper.find('button').trigger('click');
    expect(wrapper.vm.errors.credentials.password).toBe(true);
  });
});

describe('user login - login request', () => {
  it('when is an existingUser - login succes', async () => {
    const sendLoginRequest = spyOn(Login.methods, 'sendLoginRequest');
    const wrapper = mount(Login, {
      data() {
        return {
          errors: {
            'credentials': {
              'email': false,
              'password': false
            },
            'wrongCredential': false
          }
        };
      },
      props: {
        user: {
          email: 'jkahvedjian@gmail.com',
          password: '123456aA'
        }
      }
    });

    await wrapper.find('button').trigger('click');

    expect(sendLoginRequest).toHaveBeenCalled();
    expect(wrapper.vm.errors.wrongCredential).toBe(false);

    expect(wrapper.emitted()).toHaveProperty('updateIsLogged');
    expect(wrapper.emitted('updateIsLogged')[0]).toEqual([true]);
  });

  it('when is not existinguser - login fail', async () => {
    const sendLoginRequest = spyOn(Login.methods, 'sendLoginRequest');
    const wrapper = mount(Login, {
      data() {
        return {
          errors: {
            'credentials': {
              'email': false,
              'password': false
            },
            'wrongCredential': false
          }
        };
      },
      props: {
        user: {
          email: 'emailErrado@gmail.com',
          password: 'senhaErrada'
        }
      }
    });

    await wrapper.find('button').trigger('click');

    expect(sendLoginRequest).toHaveBeenCalled();
    expect(wrapper.vm.errors.wrongCredential).toBe(true);
  });
});

