import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import Login from '../Login.vue';

describe('user login - email', () => {
  it ('starts with no email error', () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    })
    expect(wrapper.vm.errors.email).toBe(false)
  })

  it ('email error true when empty', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.email).toBe(true)
  })

  it ('email error false when have @', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: 'jkahvedjian@gmail.com',
          password: ''
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.email).toBe(false)
  })

  it('email error true when does not have @', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: 'jkahvedjian',
          password: ''
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.email).toBe(true)
  })
})

describe('user login - password', () => {
  it ('starts with no password error', () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    })
    expect(wrapper.vm.errors.password).toBe(false)
  })

  it ('password error true when empty', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: ''
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.password).toBe(true)
  })

  it ('password error false when have 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '12345678'
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.password).toBe(false)
  })

  it ('password error false when have more then 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '123456789'
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.password).toBe(false)
  })

  it('password error true when have less then 8 characters', async () => {
    const wrapper = mount(Login, {
      props: {
        user: {
          email: '',
          password: '1234567'
        }
      }
    })
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.errors.password).toBe(true)
  })
})
